import socket

web_input = input('Enter the URL: ')

try:
    address = web_input.split('/')
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((address[2], 80))
    get_connection = 'GET /' + address[3] + ' HTTP/1.1\r\nHost: ' + address[2] + '\r\n\r\n'
    print(get_connection)
    cmd = get_connection.encode()
    mysock.send(cmd)

    num_char = ''
    data = ''

    while len(data) <= 3000:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end='')
        num_char = num_char + data.decode()
    
    final_char = num_char.rstrip()
    print(len(final_char))
    mysock.close()

except:
    print('URL incorrecta')