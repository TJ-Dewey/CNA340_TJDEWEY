arw_bs_ht = int(input('Enter arrow base height:\n'))
arw_bs_w = int(input('Enter arrow base width:\n'))
arw_hd_w = int(input('Enter arrow head width:\n'))

arw_cur_w = arw_bs_w

while arw_hd_w <= arw_bs_w:
    arw_hd_w = int(input('Enter arrow head width:\n'))

print('')

while arw_bs_ht > 0:
    arw_bs_ht = arw_bs_ht - 1
    while arw_cur_w > 1:
        arw_cur_w = arw_cur_w -1
        print('*', end ='')
    print('*')
    arw_cur_w = arw_bs_w
    
while arw_hd_w > 0:
    arw_hd_cur = arw_hd_w
    arw_hd_w = arw_hd_w -1
    while arw_hd_cur > 1:
        arw_hd_cur = arw_hd_cur -1
        print('*', end ='')
    print('*')    

#print('')
# Draw arrow base (height = 3, width = 2)
#print ('**')
#print ('**')
#print ('**')

# Draw arrow head (width = 4)
#print ('****')
#print ('***')
#print ('**')
#print ('*')
