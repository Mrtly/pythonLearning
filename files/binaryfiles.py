def main():
    infile = open('berlin.jpg', 'rb') #rb = read binary (t would be text)
    outfile = open('berlin-copy.jpg', 'wb')
    while True:
        buf = infile.read(10240) #that is 10k bytes, take a safe buffer size
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else: break
    outfile.close()
    print('\ndone')

if __name__ == '__main__': main()