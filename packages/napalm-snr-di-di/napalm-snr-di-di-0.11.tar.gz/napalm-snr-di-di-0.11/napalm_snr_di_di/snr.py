"""NAPALM driver for Raisecom"""

from napalm.base import NetworkDriver

import re
import collections
from napalm_snr_di_di.utils import to_seconds
from napalm.base.exceptions import ConnectionException
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)


class NapalmSnrDriver(NetworkDriver):
    platform = 'snr_di_di'

    def __init__(self, hostname, username, password, timeout=None, optional_args=None):
        self.device = {
            "device_type": "cisco_ios_telnet",
            "host": hostname,
            "username": username,
            "password": password,
            "secret": "cisco",
        }
        self.hostname = hostname

    def open(self):
        pass

    def close(self):
        pass

    def send_show_command(self, device, command, read_timeout=20):
        try:
            with ConnectHandler(**device) as telnet:
                telnet.enable()
                command = command[0]
                result = telnet.send_command(command, read_timeout=read_timeout)
            return result
        except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
            raise ConnectionException(f"Could not connect to {self.device['host']} - [{error!r}]")

    def send_show_command_onfull(self, device, command, read_timeout=20):
        try:
            with ConnectHandler(**device) as telnet:
                telnet.enable()
                command = command[0]

                telnet.send_command('terminal page-break disable')
                result = telnet.send_command(command, read_timeout=read_timeout)
                telnet.send_command('terminal page-break enable')

            return result
        except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
            raise ConnectionException(f"Could not connect to {self.device['host']} - [{error!r}]")

    def get_facts(self):
        """uptime in seconds"""

        try:
            # hostname = self.send_show_command(self.device, ["sh run | i hostname"])
            # hostname = re.search(r'hostname.*', hostname)
            # if hostname:
            #    hostname = hostname[0].replace('hostname ', '').rstrip()
            # else:
            #    hostname = ''
            hostname = ''  # убрать

            result = self.send_show_command(self.device, ["sh ver"])
            # print('********')
            # print(result)
            # print('********')

            model = re.search(r'(SNR.+) Device', result)
            if model:
                model = model[1].rstrip()
            else:
                model = ''

            serial_number = re.search(r'Serial No\.:([a-zA-Z0-9]+)', result)

            if serial_number:
                serial_number = serial_number[1].rstrip()
            else:
                serial_number = ''

            os_version = re.search(r'Soft[W,w]are Version (.+)', result)

            if os_version:
                os_version = os_version[1].rstrip()
            else:
                os_version = ''

            uptime = re.search(r'Uptime is (.+)', result)

            if uptime:
                uptime = uptime[1].rstrip()
                uptime = uptime.replace(' ', '').replace(',', '').replace('days', 'd').replace('hours', 'h').replace(
                    'minutes', 'm').replace('weeks', 'w')
                uptime = to_seconds(uptime)
            else:
                uptime = ''

            return {
                'hostname': hostname,
                'model': model,
                'vendor': 'SNR',
                'os_version': os_version,
                'serial_number': serial_number,
                'uptime': uptime,
            }
        except Exception as e:
            return {'error': str(e)}
