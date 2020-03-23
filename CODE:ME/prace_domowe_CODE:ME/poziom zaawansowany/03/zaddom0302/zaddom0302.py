# tutaj wpisz swoje imię i nazwisko file.readline().split(' - - ', 1)

def unique_ip_addresses():
    with open('apache_logs', mode='r') as file:
        IP_list = []
        line = file.readline()
        while line:
            IP_list.append(line.split(' - - ', 1)[0])
            line = file.readline()

    unique_ip_list = list(dict.fromkeys(IP_list))

    return unique_ip_list


if __name__ == '__main__':
    expected = ['66.249.73.135', '86.1.76.62', '81.220.24.207', '46.105.14.53', '207.241.237.228',
                '207.241.237.227', '50.16.19.13', '50.150.204.184', '74.125.40.20', '121.107.188.202',
                '91.177.205.119', '93.114.45.13', '200.49.190.101', '200.49.190.100', '198.46.149.143',
                '24.236.252.67', '207.241.237.225', '123.125.71.35', '209.85.238.199', '207.241.237.220',
                '207.241.237.101', '108.174.55.234', '83.149.9.216', '87.169.99.232', '218.30.103.62',
                '66.249.73.185', '67.214.178.190', '71.212.224.97', '110.136.166.128', '1.2.3.4']
    print(len(unique_ip_addresses()))
    print(unique_ip_addresses())
    print(expected)
    print(len(expected))
