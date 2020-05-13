import time 
ulang='Y' 
while ulang=='Y' or ulang=='y':
    print('\n'+'<'+'='*32+'>'+'\n'+' CALCULATE YOUR AGE  by: @ansofhn'+'\n'+'<'+'='*32+'>'+'\n')
    
    tgl=int(input('\n|>  Masukkan Tanggal Lahir anda               : '))
    bln=int(input('|>  Masukkan Bulan Lahir anda (dalam angka)   : '))
    thn=int(input('|>  Masukkan Tahun Lahir anda                 : '))
    if tgl>=32 or tgl<1 or bln>12 or bln<1:
        time.sleep(0.5)
        print('\nInput TIdak Valid..!!\n')
        time.sleep(1)
        print('Memulai Ulang Program..')
        time.sleep(1.5)
        continue
    lahir=tgl+(bln*30)+(thn*365)
    time.sleep(0.5)
    tglini=int(input('\n|>  Masukkan Tanggal Hari ini                 : '))
    blnini=int(input('|>  Masukkan Bulan Hari ini (dalam angka)     : '))
    thnini=int(input('|>  Masukkan Tahun Hari ini                   : '))
    if tglini>=32 or tglini<1 or blnini>12 or blnini<1 or thn>thnini:
        time.sleep(0.5)
        print('\nInput TIdak Valid..!!\n')
        time.sleep(1)
        print('Memulai Ulang Program..')
        time.sleep(1.5)
        continue
    aktual=tglini+(blnini*30)+(thnini*365)
#Hitungan umur
    tahun=(aktual-lahir)//365
    bulan=((aktual-lahir)%365)//30
    hari=((aktual-lahir)%365)%30
    time.sleep(0.6)
    print('\nProgram sedang bekerja...\n')
    time.sleep(1)
    print('<'*10,'Umur anda saat ini adalah :',tahun,'Tahun',bulan,'Bulan',hari,'Hari','>'*10,'\n')
    print('='*48)
    ulang = input ('Apakah anda ingin lanjut menghitung? (Y/N): ')
    if ulang == 'N' or ulang == 'n' or ulang == 'no' or ulang == 'NO':
        print("\nProgram Berakhir, Terima kasih sudah menggunakan Program ini\n")
        break