f=open('pr.txt','r')
open('r1.txt', 'w').close()
f1=open('r1.txt','a')
def isint(x):
    try:
        int(x)
        return True
    except ValueError:
        return False
"""
cos(x)
"""
def cos(a):
    coef=''
    ind=''
    otv=''
    c=0
    lala=''
    chet=0
    t=''
    if 'cos' in a:
        if '^' not in a:
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
                                t+=i
                                if i=='y':
                                    ind+='y'
                            elif i == '/':
                                ind+=i
                            else:
                                ind+=i
                        if '/' in ind:
                            f1.write(str(t)+'=(pi/2*'+str(ind)+'+(pi*n)/'+str(ind)+'. n принадлежит Z'+'\n')
                        else:
                            if ind!='' and '/' not in ind and 'y' not in ind:
                                ind=int(ind)
                            if otv=='0':
                                if isint(ind)==True:
                                    f1.write(str(t)+'=(pi/'+str(2*ind)+')+(pi/'+str(ind)+')*n. n принадлежит Z'+'\n')
                                else:
                                    f1.write(str(t)+'=(pi/2)+pi*n. n принадлежит Z'+'\n')
                            elif otv=='1':
                                if isint(ind)==True:
                                    f1.write(str(t)+'=(pi*n)/'+str(2*ind)+'. n принадлежит Z'+'\n')
                                else:
                                    f1.write(str(t)+'=2*pi*n. n принадлежит Z'+'\n')
                            elif otv=='1/2':
                                if isint(ind)==True:
                                    f1.write(str(t)+'=+-(pi/'+str(3*ind)+')+(pi*n)/'+str(2*ind)+'. n принадлежит Z'+'\n')
                                else:
                                    f1.write(str(t)+'=+-(pi/3)+2*pi*n. n принадлежит Z'+'\n')
                            elif otv=='sqrt(2)/2':
                                if isint(ind)==True:
                                    f1.write(str(t)+'=+-(pi/'+str(4*ind)+')+(pi*n)/'+str(2*ind)+'. n принадлежит Z'+'\n')
                                else:
                                    f1.write('x=+-(pi/4)+2*pi*n. n принадлежит Z'+'\n')
                            elif otv=='sqrt(3)/3':
                                if isint(ind)==True:
                                    f1.write(str(t)+'=+-(pi/'+str(6*ind)+')+(pi*n)/'+str(2*ind)+'. n принадлежит Z'+'\n')
                                else:
                                    f1.write(str(t)+'=+-(pi/6)+2*pi*n. n принадлежит Z'+'\n')
                            elif otv=='-1/2':
                                if isint(ind)==True:
                                    f1.write(str(t)+'=+-(2*pi)/'+str(3*ind)+'(+2*pi*n)/'+str(ind)+'. n принадлежит Z'+'\n')
                                else:
                                    f1.write(str(t)+'=+-(2*pi)/3+2*pi*n. n принадлежит Z'+'\n')

"""
sin(x)
"""
def sin(a):
    coef=''
    ind=''
    otv=''
    c=0
    lala=''
    chet=0
    t=''
    if 'sin' in a:
        if 'cos' not in a:
            if 'tg' not in a:
                if 'ctg' not in a:
                    if '+' not in a:
                        if '-' not in a:
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
                            c=0
                            for i in coef:
                                if i.isalpha():
                                    t+=i
                                    if i=='y' and '/' in a:
                                        ind+='y'
                                elif i == '/':
                                    ind+=i
                                else:
                                    ind+=i
                            if '/' in ind:
                                    f1.write(str(t)+'=(pi*n)/'+str(ind)+'. n принадлежит Z'+'\n')
                                    c=1
                            if ind!='' and '/' not in ind and c!=1:
                                if 'y' not in ind:
                                    ind=int(ind)
                            if c==0:
                                if otv=='0':
                                    if isint(ind)==True:
                                        f1.write(str(t)+'=(pi*n)/'+str(ind)+'. n принадлежит Z'+'\n')
                                    else:
                                        f1.write(str(t)+'=pi*n. n принадлежит Z'+'\n')
                                elif otv=='1':
                                    if isint(ind)==True:
                                        f1.write(str(t)+'=(pi/'+str(2*ind)+')+(pi*n)/'+str(ind*2)+'. n принадлежит Z'+'\n')
                                    else:
                                        f1.write(str(t)+'=(pi/2)+2*pi*n. n принадлежит Z'+'\n')
                                elif otv=='1/2':
                                    if isint(ind)==True:
                                        f1.write(str(t)+'=(-1)^n*(pi/'+str(ind*6)+')+ pi * n. n принадлежит Z'+'\n')
                                    else:
                                        f1.write(str(t)+'=(-1)^n*pi/6+pi*n. n принадлежит Z'+'\n')
                                elif otv=='sqrt(3)/3':
                                    if isint(ind)==True:
                                        f1.write(str(t)+'=(-1)^n*(pi/'+str(ind*3)+')+(pi*n)/'+str(ind)+'. n принадлежит Z'+'\n')
                                    else:
                                        f1.write(str(t)+'=(-1)^n*(pi/3)+pi*n. n принадлежит Z'+'\n')
                                elif otv=='sqrt(2)/2':
                                    if isint(ind)==True:
                                        f1.write(str(t)+'=(-1)^n*(pi/'+str(ind*4)+'(pi*n)/'+str(ind)+'. n принадлежит Z'+'\n')
                                    else:
                                        f1.write(str(t)+'=(-1)^n*(pi/4)+pi*n. n принадлежит Z'+'\n')
                                elif otv == '-1/2':
                                    if isint(ind)==True:
                                        f1.write(str(t)+'=7pi/'+str(ind*6)+'+(2*pi*n)/'+str(ind)+';11pi/'+str(ind*6)+'+(2*pi*n)/'+str(ind)+'. n принадлежит Z'+'\n')
                                    else:
                                        f1.write(str(t)+'=7pi/6+2*pi*n;11pi/6+2*pi*n. n принадлежит Z'+'\n')
"""
tg(x)
"""
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
                    	if isint(ind)==True:
                    		f1.write('x=pi/'+str(ind*3)+'+(pi*n)/'+str(ind)+'. n принадлежит Z'+'\n')
"""
ctg(x)
"""
                            
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
"""
cos(x)*sin(y)
"""
def cossin(a):
    if 'cos' in a:
        if 'sin' in a:
            if '/' not in a:
                if '^' not in a:
                    if '+' not in a:
                        if '-' not in a:
                                coef1=''
                                coef2=''
                                ind1=''
                                ind2=''
                                otv=''
                                c=0
                                lala=''
                                chet=0
                                if 'y' in a:
                                    c=1
                                for i in a:
                                    if i=='(':
                                        if chet==3:
                                            chet=2
                                        else:
                                            chet=1
                                    elif i==')':
                                        chet=3
                                    elif chet==1:
                                        if i=='y':
                                            coef1+='x'
                                        else:
                                            coef1+=i
                                    elif chet==2:
                                        if i=='y':
                                            coef2+='x'
                                        else:
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
                                    if c==1:
                                        pr1=''
                                        pr1+='cos'+'('+coef1+')='+otv
                                        pr2=''
                                        pr2+='sin'+'('+coef2+')='+otv
                                        cos(pr1)
                                        sin(pr2)
"""
cos(2x)-cos^2(x)
"""
def cosmcos(a):
    if 'cos' in a:
        if '^' in a:
            if '-' in a:
                if 'sin' not in a:
                    k=0
                    koef1=''
                    koef2=''
                    fkoef=''
                    otv=''
                    for i in a:
                        if i == '(' and k==0:
                            k=1
                        elif k == 1 and i!=')':
                            koef1+=i
                        elif i == ')' and k==1:
                            k=2
                        elif i == '(' and k==2:
                            k=3
                        elif k == 3 and i!=')':
                            koef2+=i
                        elif k == 3 and i == ')':
                            break
                    for i in koef2:
                        if i.isdigit():
                            fkoef+=i
                    for i in a:
                        if i == '=':
                            k=-1
                        elif k == -1 and i!=' ' and i!='\n':
                            otv+=i
                    if '/' in otv:
                        f1.write('Не имеет решения(('+'\n')
                    elif '0' in otv:
                        if fkoef!='':
                            f1.write('x=pi*n. n принадлежит Z'+'\n')
                        else:
                            f1.write('x=(pi*n)/'+fkoef+'. n принадлежит Z'+'\n')
'''
cos(2x) + sin^2(x)
'''
def cospsin(a):
    if 'cos' in a:
        if 'sin' in a:
            if '+' in a:
                if '^' in a:
                    k=0
                    koef1=''
                    koef2=''
                    fkoef=''
                    otv=''
                    for i in a:
                        if i == '(' and k==0:
                            k=1
                        elif k == 1 and i!=')':
                            koef1+=i
                        elif i == ')' and k==1:
                            k=2
                        elif i == '(' and k==2:
                            k=3
                        elif k == 3 and i!=')':
                            koef2+=i
                        elif k == 3 and i == ')':
                            break
                    for i in koef2:
                        if i.isdigit():
                            fkoef+=i
                    for i in a:
                        if i == '=':
                            k=-1
                        elif k == -1 and i!=' ' and i!='\n':
                            otv+=i
                    if otv == '1/4':
                        if fkoef != '':
                            f1.write('x=pi/4+(pi*n)/4. n принадлежит Z'+'\n')
                        else:
                            p1='cos('+koef1+')=1/2'
                            cos(p1)
                            p2='cos('+koef1+')=-1/2'
                            cos(p2)
                    elif otv == '1/2':
                        if fkoef != '':
                            f1.write('x=pi/'+str(fkoef)+'(pi*n)/'+str(2*fkoef)+'. n принадлежит Z'+'\n')
                        else:
                            f1.write('x=pi/4+(pi*n)/2. n принадлежит Z'+'\n')
                    elif otv == '1/3':
                        p1='cos('+fkoef+')=sqrt(3)/3'
                        cos(p1)
                    elif otv == '1':
                        if fkoef!='':
                            f1.write('x=(pi*n)/'+str(fkoef)+'. n принадлежит Z'+'\n')
                        else:
                            f1.write('x=pi*n. n принадлежит Z'+'\n')
                    elif otv == '0':
                        if fkoef!='':
                            f1.write('x=pi/'+str(fkoef*2)+'(pi*n)/'+str(fkoef)+'. n принадлежит Z'+'\n')
                        else:
                            f1.write('x=pi/2+pi*k. n принадлежит Z'+'\n')
'''
sin(2x) +(-) cos(x)
'''
def sincos(a):
    if 'sin' in a:
        if 'cos' in a:
            if '+' or '-' in a:
                if '0' in a:
                    if '^' not in a:
                        k=0
                        koef1=''
                        koef2=''
                        fkoef2=''
                        fkoef1=''
                        otv=''
                        for i in a:
                            if i == '(' and k==0:
                                k=1
                            elif k == 1 and i!=')':
                                koef1+=i
                            elif i == ')' and k==1:
                                k=2
                            elif i == '(' and k==2:
                                k=3
                            elif k == 3 and i!=')':
                                koef2+=i
                            elif k == 3 and i == ')':
                                break
                        for i in koef1:
                            if i.isdigit():
                                fkoef1+=i
                        for i in koef2:
                            if i.isdigit():
                                fkoef2+=i
                        for i in a:
                            if i == '=':
                                k=-1
                            elif k == -1 and i!=' ' and i!='\n':
                                otv+=i
                        if fkoef2 == '':
                            if '-' in a:
                                p1='cos(x)=0'
                                p2='sin(x)=1/2'
                                cos(p1)
                                sin(p2)
                            elif '+' in a:
                                p1='cos(x)=0'
                                p2='sin(x)=-1/2'
                                cos(p1)
                                sin(p2)
                        else:
                            if '-' in a:
                                p1='cos('+koef2+')=0'
                                p2='sin('+koef2+')=1/2'
                                cos(p1)
                                sin(p2)
                            elif '+' in a:
                                p1='cos('+koef2+')=0'
                                p2='sin('+koef2+')=-1/2'
                                cos(p1)
                                sin(p2)
"""
Функция решения sin(2x) +(-) sin(x)
"""
def sinsin(a):
    if 'sin' in a:
        if 'cos' not in a:
            if '+' or '-' in a:
                if '0' in a:
                    if '^' not in a:
                        k=0
                        koef1=''
                        koef2=''
                        fkoef2=''
                        fkoef1=''
                        otv=''
                        for i in a:
                            if i == '(' and k==0:
                                k=1
                            elif k == 1 and i!=')':
                                koef1+=i
                            elif i == ')' and k==1:
                                k=2
                            elif i == '(' and k==2:
                                k=3
                            elif k == 3 and i!=')':
                                koef2+=i
                            elif k == 3 and i == ')':
                                break
                        for i in koef1:
                            if i.isdigit():
                                fkoef1+=i
                        for i in koef2:
                            if i.isdigit():
                                fkoef2+=i
                        for i in a:
                            if i == '=':
                                k=-1
                            elif k == -1 and i!=' ' and i!='\n':
                                otv+=i
                        if fkoef2 == '':
                            if '-' in a:
                                p1='sin(x)=0'
                                p2='cos(x)=-1/2'
                                cos(p2)
                                sin(p1)
                            elif '+' in a:
                                p1='sin(x)=0'
                                p2='cos(x)=1/2'
                                cos(p2)
                                sin(p1)
                        else:
                            if '+' in a:
                                p1='sin('+koef2+')=0'
                                p2='cos('+koef2+')=1/2'
                                cos(p2)
                                sin(p1)
                            elif '-' in a:
                                p1='sin('+koef2+')=0'
                                p2='cos('+koef2+')=-1/2'
                                cos(p2)
                                sin(p1)
'''
cos(x)*sin(y)
'''

def cosasin(a):
    if 'cos' in a:
        if 'sin' in a:
            if '/' in a:
                if '0' in a:
                    k=0
                    koef1=''
                    koef2=''
                    for i in a:
                        if i == '(' and k==0:
                            k=1
                        elif k == 1 and i!=')':
                            koef1+=i
                        elif i == ')' and k==1:
                            k=2
                        elif i == '(' and k==2:
                            k=3
                        elif k == 3 and i!=')':
                            koef2+=i
                        elif k == 3 and i == ')':
                            break
                    p1='cos('+koef1+')=0'
                    p2='sin('+koef2+')=0'
                    cos(p1)
                    sin(p2)
'''
tg(x)*cos(y)
'''
def tgcos(a):
    if 'tg' in a:
        if 'cos' in a:
            if 'sin' not in a:
                k=0
                koef1=''
                koef2=''
                fkoef1=''
                otv=''
                for i in a:
                    if i == '(' and k==0:
                        k=1
                    elif k == 1 and i!=')':
                        koef1+=i
                    elif i == ')' and k==1:
                        k=2
                    elif i == '(' and k==2:
                        k=3
                    elif k == 3 and i!=')':
                        koef2+=i
                    elif k == 3 and i == ')':
                        break
                for i in koef1:
                    if i.isdigit():
                       fkoef1+=i
                for i in a:
                    if i == '=':
                        k=-1
                    elif k == -1 and i!=' ' and i!='\n':
                        otv+=i
                if otv == 'sqrt(3)':
                    f1.write('Нет решения((('+'\n')
                else:
                    if fkoef1!='':
                        p1='sin('+koef1+')='+otv
                        sin(p1)
                    else:
                        p1='sin(x)='+otv
                        sin(p1)
'''
ctg(x)*sin(x)
'''
def ctgsin(a):
    if 'ctg' in a:
        if 'sin' in a:
            if '*' in a:
                k=0
                koef1=''
                koef2=''
                fkoef1=''
                otv=''
                for i in a:
                    if i == '(' and k==0:
                        k=1
                    elif k == 1 and i!=')':
                        koef1+=i
                    elif i == ')' and k==1:
                        k=2
                    elif i == '(' and k==2:
                        k=3
                    elif k == 3 and i!=')':
                        koef2+=i
                    elif k == 3 and i == ')':
                        break
                for i in koef1:
                    if i.isdigit():
                       fkoef1+=i
                for i in a:
                    if i == '=':
                        k=-1
                    elif k == -1 and i!=' ' and i!='\n':
                        otv+=i
                if otv == 'sqrt(3)':
                    f1.write('Нет решения((('+'\n')
                else:
                    if fkoef1!='':
                        p1='cos('+koef1+')='+otv
                        cos(p1)
                    else:
                        p1='cos(x)='+otv
                        cos(p1)


invinit=0
for a in f:
        invinit+=1
        f1.write(str(invinit)+' пример'+'\n')
        cos(a)
        sin(a)
        tg(a)
        ctg(a)
        cossin(a)
        cosmcos(a)
        cospsin(a) 
        sincos(a)
        sinsin(a)
        cosasin(a)
        tgcos(a)
        ctgsin(a)
f1.close()