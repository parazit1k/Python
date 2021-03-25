f=open('pr.txt','r')
open('r1.txt', 'w').close()
f1=open('r1.txt','a')
def isint(x):
    try:
        int(x)
        return True
    except ValueError:
        return False
def cos(a):
    coef=''
    ind=''
    otv=''
    c=0
    lala=''
    chet=0
    if 'cos' in a:
        if 'sin' not in a:
            if 'tg' not in a:
                if 'ctg' not in a:
                    for i in a:
                        if c==0 and i!='(':
                            continue
                        elif i=='(':
                            c+=1
                        elif c==1 and i!=')':
                            coef+=i
                        elif i==')':
                            c+=1
                        elif i=='=':
                            continue
                        elif c==2:
                            if 'sqrt(2)/2' in a and chet==0:
                                otv+='sqrt(2)/2'
                                chet+=1
                            elif 'sqrt(3)/3' in a and chet==0:
                                otv+='sqrt(3)/3'
                                chet+=1
                            else:
                                if i!=' ' and i!='\n' and chet==0:
                                    otv+=i
                    for i in coef:
                        if i.isalpha():
                            continue
                        else:
                            ind+=i
                    if ind!='':
                        ind=int(ind)
                    if otv=='0':
                        if isint(ind)==True:
                            f1.write('x=(pi/'+str(2*ind)+')+(pi/'+str(ind)+')*n. n принадлежит Z'+'\n')
                        else:
                            f1.write('x=(pi/2)+pi*n. n принадлежит Z'+'\n')
                    elif otv=='1':
                        if isint(ind)==True:
                            f1.write('x=(pi*n)/'+str(2*ind)+'. n принадлежит Z'+'\n')
                        else:
                            f1.write('x=2*pi*n. n принадлежит Z'+'\n')
                    elif otv=='1/2':
                        if isint(ind)==True:
                            f1.write('x=+-(pi/'+str(3*ind)+')+(pi*n)/'+str(2*ind)+'. n принадлежит Z'+'\n')
                        else:
                            f1.write('x=+-(pi/3)+2*pi*n. n принадлежит Z'+'\n')
                    elif otv=='sqrt(2)/2':
                        if isint(ind)==True:
                            f1.write('x=+-(pi/'+str(4*ind)+')+(pi*n)/'+str(2*ind)+'. n принадлежит Z'+'\n')
                        else:
                            f1.write('x=+-(pi/4)+2*pi*n. n принадлежит Z'+'\n')
                    elif otv=='sqrt(3)/3':
                        if isint(ind)==True:
                            f1.write('x=+-(pi/'+str(6*ind)+')+(pi*n)/'+str(2*ind)+'. n принадлежит Z'+'\n')
                        else:
                            f1.write('x=+-(pi/6)+2*pi*n. n принадлежит Z'+'\n')
def sin(a):
    coef=''
    ind=''
    otv=''
    c=0
    lala=''
    chet=0
    if 'sin' in a:
        if 'cos' not in a:
            if 'tg' not in a:
                if 'ctg' not in a:
                    for i in a:
                        if c==0 and i!='(':
                            continue
                        elif i=='(':
                            c+=1
                        elif c==1 and i!=')':
                            coef+=i
                        elif i==')':
                            c+=1
                        elif i=='=':
                            continue
                        elif c==2:
                            if 'sqrt(2)/2' in a and chet==0:
                                otv+='sqrt(2)/2'
                                chet+=1
                            elif 'sqrt(3)/3' in a and chet==0:
                                otv+='sqrt(3)/3'
                                chet+=1
                            else:
                                if i!=' ' and i!='\n' and chet==0:
                                    otv+=i
                    for i in coef:
                        if i.isalpha():
                            continue
                        else:
                            ind+=i
                    if ind!='':
                        ind=int(ind)
                    if otv=='0':
                        if isint(ind)==True:
                            f1.write('x=(pi*n)/'+str(ind)+'. n принадлежит Z'+'\n')
                        else:
                            f1.write('x=pi*n. n принадлежит Z'+'\n')
                    elif otv=='1':
                        if isint(ind)==True:
                            f1.write('x=(pi/'+str(2*ind)+')+(pi*n)/'+str(ind*2)+'. n принадлежит Z'+'\n')
                        else:
                            f1.write('x=(pi/2)+2*pi*n. n принадлежит Z'+'\n')
                    elif otv=='1/2':
                        if isint(ind)==True:
                            f1.write('x=(-1)^n*(pi/'+str(ind*6)+')+ pi * n. n принадлежит Z'+'\n')
                        else:
                            f1.write('x=(-1)^n*pi/6+pi*n. n принадлежит Z'+'\n')
                    elif otv=='sqrt(3)/3':
                        if isint(ind)==True:
                            f1.write('x=(-1)^n*(pi/'+str(ind*3)+')+(pi*n)/'+str(ind)+'. n принадлежит Z'+'\n')
                        else:
                            f1.write('x=(-1)^n*(pi/3)+pi*n. n принадлежит Z'+'\n')
                    elif otv=='sqrt(2)/2':
                        if isint(ind)==True:
                            f1.write('x=(-1)^n*(pi/'+str(ind*4)+'(pi*n)/'+str(ind)+'. n принадлежит Z'+'\n')
                        else:
                            f1.write('x=(-1)^n*(pi/4)+pi*n. n принадлежит Z'+'\n')
def tg(a):
    coef=''
    ind=''
    otv=''
    c=0
    lala=''
    chet=0
    if 'tg' in a:
        if 'cos' not in a:
            if 'sin' not in a:
                if 'ctg' not in a:
                    for i in a:
                        if c==0 and i!='(':
                            continue
                        elif i=='(':
                            c+=1
                        elif c==1 and i!=')':
                            coef+=i
                        elif i==')':
                            c+=1
                        elif i=='=':
                            continue
                        elif c==2:
                            if 'sqrt(3)' in a and chet==0:
                                if '/3' not in a:
                                    otv='sqrt(3)'
                                    chet+=1
                                elif 'sqrt(3)/3' in a:
                                    otv='sqrt(3)/3'
                                    chet+=1
                            else:
                                if i!=' ' and i!='\n' and chet==0:
                                    otv+=i
                    for i in coef:
                        if i.isalpha():
                            continue
                        else:
                            ind+=i
                    if ind!='':
                        ind=int(ind)
                    if otv=='0':
                        if isint(ind)==True:
                            f1.write('x='+str(ind)+'*pi*n. n принадлежит Z'+'\n')
                        else:
                            f1.write('x=pi*n. n принадлежит Z'+'\n')
                    elif otv=='1':
                        if isint(ind)==True:
                            f1.write('x=(pi/'+str(4*ind)+')+(pi*n)/'+str(ind)+'. n принадлежит Z'+'\n')
                        else:
                            f1.write('x=(pi)/4+pi*n. n принадлежит Z'+'\n')
                    elif otv=='sqrt(3)/3':
                        if isint(ind)==True:
                            f1.write('x=(pi/'+str(6*ind)+')+(pi*n)/'+str(ind)+'. n принадлежит Z'+'\n')
                        else:
                            f1.write('x=(pi/6)+pi*n. n принадлежит Z'+'\n')
                    elif otv=='sqrt(3)':
                    	if isind(ind)==True:
                    		f1.write('x')
                            
def ctg(a):
    coef=''
    ind=''
    otv=''
    c=0
    lala=''
    chet=0
    if 'ctg' in a:
        if 'cos' not in a:
            if 'sin' not in a:
                for i in a:
                    if c==0 and i!='(':
                        continue
                    elif i=='(':
                        c+=1
                    elif c==1 and i!=')':
                        coef+=i
                    elif i==')':
                        c+=1
                    elif i=='=':
                        continue
                    elif c==2:
                        if 'sqrt(3)' in a and chet==0:
                            if '/3' not in a:
                                otv+='sqrt(3)'
                                chet+=1
                            elif 'sqrt(3)/3' in a and chet==0:
                                otv+='sqrt(3)/3'
                                chet+=1
                        else:
                            if i!=' ' and i!='\n' and chet==0:
                                otv+=i
                for i in coef:
                    if i.isalpha():
                        continue
                    else:
                        ind+=i
                if ind!='':
                    ind=int(ind)
                if otv=='0':
                    if isint(ind)==True:
                        f1.write('x=(pi/'+str(ind*2)+')+(pi*n)/'+str(ind)+'. n принадлежит Z'+'\n')
                    else:
                        f1.write('x=(pi/2)+pi*n. n принадлежит Z'+'\n')
                elif otv=='1':
                    if isint(ind)==True:
                        f1.write('x=(pi/'+str(ind*4)+')+(pi*n)/'+str(ind)+'. n принадлежит Z'+'\n')
                    else:
                        f1.write('x=(pi/4)+pi*n. n принадлежит Z'+'\n')
                elif otv=='sqrt(3)/3':
                    if isint(ind)==True:
                        f1.write('x=(pi/'+str(ind*3)+')+(pi*n)/'+str(ind)+'. n принадлежит Z'+'\n')
                    else:
                        f1.write('x=(pi/3)+pi*n. n принадлежит Z'+'\n')
                elif otv=='sqrt(3)':
                    if isint(ind)==True:
                        f1.write('x=(pi/'+str(ind*6)+')+(pi*n)/'+str(ind)+'. n принадлежит Z'+'\n')
                    else:
                        f1.write('x=(pi/6)+pi*n. n принадлежит Z'+'\n')
def cossin(a):
    coef1=''
    coef2=''
    ind1=''
    ind2=''
    otv=''
    c=0
    lala=''
    chet=0
    for i in a:
        if i=='(':
            if chet==3:
                chet=2
            else:
                chet=1
        elif i==')':
            chet=3
        elif chet==1:
            coef1+=i
        elif chet==2:
            coef2+=i
    for i in a:
        if i=='=':
            chet=1
        elif chet==1:
            if i!='' and i!=' ' and i!='\n':
                otv+=i
    for i in coef1:
        if i.isdigit():
            ind1+=i
    for i in coef2:
        if i.isdigit():
            ind2+=i
    if otv=='0':
        pr1=''
        pr1+='cos'+'('+coef1+')='+otv
        pr2=''
        pr2+='sin'+'('+coef2+')='+otv
        cos(pr1)
        sin(pr2)
def cos-cos(a):
    if 'cos' in a:
        if '^' in a:
            if '-' in a:
                if 'cos(2x) - cos^2(x)' or  in a:
                    if '0' in a:
                        per='sin(x)=0'
                        sin(per)
                    elif '1/2' in a:
                        per='sin(x)=1/2'
                        sin(per)

invinit=0
for a in f:
    invinit+=1
    f1.write(str(invinit)+' пример'+'\n')
    cos(a)
    sin(a)
    tg(a)
    ctg(a)
    if 'cos' in a:
        if 'sin' in a:
            if '/' not in a:
                if '^' not in a:
                    cossin(a)
            elif '/' in a:
                if '^' in a:
                    *
                elif '^' not in a:
                    *

                
            
f1.close()