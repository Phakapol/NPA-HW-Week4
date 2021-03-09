from netmiko import ConnectHandler

def cdpInterfaceDescription():
    """cdp and interface description"""
    cdp_output = ssh.send_command('sh cdp nei')
    outputList = []
    outputList = cdp_output.splitlines()
    info_line = []
    for line in outputList:
        if "npa.com" in line:
            CdpOutputLine = str(line).split()
            info_line.append(CdpOutputLine)
    file_name = 'int_description/device' + str(device_num) + '.txt'
    f = open(file_name, "w")
    for member in info_line:
        line = 'cdp run\n'
        f.write(line)
        line = 'int ' + member[1] + member[2] + '\n'
        f.write(line)
        line = 'description ' + 'connect to ' + member[-2] + member[-1] + ' of ' + member[0].split('.')[0] + '\n'
        f.write(line)
    f.close()
    config_sent = ssh.send_config_from_file(config_file=file_name)
    print(config_sent)


username = 'admin'
password = 'cisco'

for device_num in range(1, 10):
    device_ip = '172.31.175.' + str(device_num)
    device_par = {'device_type': 'cisco_ios',
                  'ip': device_ip,
                  'username': username,
                  'password': password,
                  }

    with ConnectHandler(**device_par) as ssh:
        """config loopback / ACL for ssh / CDP interface description"""
        if device_num == 1:
            file_config = 'R0.txt'
            config_sent = ssh.send_config_from_file(config_file=file_config)
            print(config_sent)
        elif device_num == 2:
            file_config = 'S0.txt'
            config_sent = ssh.send_config_from_file(config_file=file_config)
            print(config_sent)
        elif device_num == 3:
            file_config = 'S1.txt'
            config_sent = ssh.send_config_from_file(config_file=file_config)
            print(config_sent)
        elif device_num == 4:
            file_config = 'R1.txt'
            config_sent = ssh.send_config_from_file(config_file=file_config)
            print(config_sent)
        elif device_num == 5:
            file_config = 'R2.txt'
            config_sent = ssh.send_config_from_file(config_file=file_config)
            print(config_sent)
        elif device_num == 6:
            file_config = 'R3.txt'
            config_sent = ssh.send_config_from_file(config_file=file_config)
            print(config_sent)
        elif device_num == 7:
            file_config = 'R4.txt'
            config_sent = ssh.send_config_from_file(config_file=file_config)
            print(config_sent)
        elif device_num == 8:
            file_config = 'S2.txt'
            config_sent = ssh.send_config_from_file(config_file=file_config)
            print(config_sent)
        elif device_num == 9:
            file_config = 'R5.txt'
            config_sent = ssh.send_config_from_file(config_file=file_config)
            print(config_sent)



        cdpInterfaceDescription()
        """show interface brief and save config"""
        result = ssh.send_command('sh ip int br')
        print(result)
        ssh.send_command('write')  



