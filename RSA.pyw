# Emre Ovunc
# Izmir University of Economics
# Computer Engineering
# E-mail: info@emreovunc.com
# CE 340 S.KONDAKCI

from Tkinter import *
import tkMessageBox
import tkFileDialog
import rsa

def main_menu():
        
        def PrivateKey_Func():
                tkMessageBox.showinfo("Private Key", private_key)
                
        def PublicKey_Func():
                tkMessageBox.showinfo("Public Key", public_key)
 
        def Encrypt():              
                EncryptFile.config(state=NORMAL)
                EncryptFile.delete("0.0",END)
                tempdir = tkFileDialog.askopenfilename(title='Please select a text file:')
                EncryptFile.insert(END,tempdir)
                EncryptFile.config(state=DISABLED)
                with open(tempdir, 'r+') as f:
                        Inputs = f.read()
                ascii_Text="1"
                for x in range(0,len(Inputs)):
                        if ord(Inputs[x])<100:
                                ascii_Text+="0"+str(ord(Inputs[x]))
                        else:
                                ascii_Text+=str(ord(Inputs[x]))
                crypto=rsa.encrypt(ascii_Text,public_key)
                file = open("/home/debian/Desktop/Encrypted-Output.txt", "w")
                file.write(crypto)
                file.close()
                
        def Decrypt():
                DecryptFile.config(state=NORMAL)
                DecryptFile.delete("0.0",END)
                tempdir = tkFileDialog.askopenfilename(title='Please select a text file:')
                DecryptFile.insert(END,tempdir)
                DecryptFile.config(state=DISABLED)
                with open(tempdir, 'r+') as f:
                        Inputs = f.read()
                Inputs = rsa.decrypt(Inputs, private_key)
                msg=""
                for x in range (1,len(Inputs),3):
                        if Inputs[x]=="0":
                                msg+=chr(int(Inputs[x+1:x+3]))
                        else:
                                msg+=chr(int(Inputs[x:x+3]))
                file = open("/home/debian/Desktop/Decrypted-Output.txt", "w")
                file.write(msg)
                file.close()

        menu_main=Tk()
        menu_main.title("RSA Encrypt & Decrypt")
        menu_main.geometry("300x190")
        menu_main.resizable(width=FALSE,height=FALSE)

        keyLabel=Label(text="Show Keys",font=("Arial",8,"bold"))
        keyLabel.place(x=100,y=10)

        PrivateKey_Button=Button(text="Private Key",command=PrivateKey_Func,font=("Arial",8,"bold"),fg="green",height=1,width=12)
        PrivateKey_Button.place(x=15,y=34)

        PublicKey_Button=Button(text="Public Key",command=PublicKey_Func,font=("Arial",8,"bold"),fg="green",height=1,width=12)
        PublicKey_Button.place(x=165,y=34)

        Encrypt_Label=Label(text="Select Text File to Encrypt: ",font=("Arial",8,"bold"))
        Encrypt_Label.place(x=10,y=80)

        Encrypt_Button=Button(text="Encrypt",command=Encrypt,font=("Arial",8),fg="blue",height=1,width=7)
        Encrypt_Button.place(x=200,y=95)

        EncryptFile=Text(height=1,width=26)
        EncryptFile.place(x=10,y=100)
        EncryptFile.config(state=DISABLED)

        Decrypt_Label=Label(text="Select Text File to Decrypt: ",font=("Arial",8,"bold"))
        Decrypt_Label.place(x=10,y=130)

        Decrypt_Button=Button(text="Decrypt",command=Decrypt,font=("Arial",8),fg="red",height=1,width=7)
        Decrypt_Button.place(x=200,y=145)

        DecryptFile=Text(height=1,width=26)
        DecryptFile.place(x=10,y=150)
        DecryptFile.config(state=DISABLED)

        EmreOvunc=Label(text="EmreOvunc 2015 ",font=("Arial",6),fg="gray")
        EmreOvunc.place(x=105,y=173)
        
        (public_key, private_key) = rsa.newkeys(1024)

main_menu()
mainloop()



