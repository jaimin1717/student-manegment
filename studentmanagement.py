# -----------all copyright reserved by daksh,mayank,jaimin,shruti. with 25% equity each person--------# #----our database name is:-ict24    , table nameis :-ictstudent1 #
def addstudeent():
    def submitadd():        
        branch = branchval.get()
        enrollno = enrollnoval.get()
        name = nameval.get()
        dob = dobval.get()
        sem = semesterval.get()
        detained = detainedval.get()
        mobile = mobileval.get()
        gender = genderval.get()
        parentsname = parents_nameval.get()
        parentsno = parents_noval.get()
        email = emailval.get()
        adharno = adharval.get()   
        abcid = abcidval.get()
        category = categoryval.get()
        physicalhandi = phval.get()
        percity = percityval.get()
        perdistrict = perdistrictval.get()
        perpin = perpinval.get()
        precity = precityval.get()
        predistrict = predistictval.get()
        prepin = prepinval.get()
        cpi = cpival.get()
        spi = spival.get()
        sscyear = ssc_yr_val.get()
        sscpercentage = ssc_per_val.get()
        hscyear = hsc_yr_val.get()
        hscpercentage = hsc_per_val.get()
        itiyear = iti_yr_val.get()
        itipercentage = iti_per_val.get()
         # Validate the enrollment number
        if not (enrollno.isdigit() and len(enrollno) == 12):
            messagebox.showerror('Notification', 'Enrollment number must be exactly 12 digits.', parent=addroot)
            return
        try:
            strr = 'insert into ictstudent1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'#29
            mycursor.execute(strr,(branch,enrollno,name,dob,sem,detained,mobile,gender,parentsname,parentsno,email,adharno,abcid,category,physicalhandi,percity,perdistrict,perpin,precity,predistrict,prepin,cpi,spi,sscyear,sscpercentage,hscyear,hscpercentage,itiyear,itipercentage))
            con.commit()    
            res = messagebox.askyesnocancel('Notification','Enroll {} Name {} Added suucessfull..and want to clean a form?'.format(enrollno,name),parent=addroot)
            if(res==True):
                branchval.set('')
                enrollnoval.set('')
                nameval.set('')
                dobval.set('')
                semesterval.set('')
                detainedval.set('')
                mobileval.set('')
                genderval.set('')
                parentsnameval.set('')
                parentsnoval.set('')
                emailval.set('')
                adharval.set('')   
                abcidval.set('')
                categoryval.set('')
                phval.set('')
                percityval.set('')
                perdistrictval.set('')
                perpinval.set('')
                precityval.set('')
                predistictval.set('')
                prepinval.set('')
                cpival.set('')
                spival.set('')
                ssc_yr_val.set('')
                ssc_per_val.set('')
                hsc_yr_val.set('')
                hsc_per_val.set('')
                iti_yr_val.set('')
                iti_per_val.set('')

        except:            
            messagebox.showerror('Notification','Enroll {} Already Exit...'.format(enrollno),parent=addroot)
            strr='select * from ictstudent1'
            mycursor.execute(strr)
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25],i[26],i[27],i[28]]
                studenttable.insert('', END, values=vv)
                print(datas)
        
        
            
        #---------------------#
    #add function#
    addroot = Toplevel(master=entry_frame)
    addroot.grab_set()
    addroot.geometry("980x800+220+200")
    addroot.title("student I.C.T Mnagement system")
    addroot.config(bg='blue')
    addroot.resizable(False,False)
#==================ADD SYSTEM LABELS=================#
    
    #=======s=================add label===================#
    
    branchlable=Label(addroot,text="Enter Branch:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    branchlable.grid(row=0,column=0)

    enrollnolable=Label(addroot,text="Enrollment no:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    enrollnolable.grid(row=1,column=0)

    namelable=Label(addroot,text="Name:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelable.grid(row=2,column=0)

    doblable=Label(addroot,text="D.o.b:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblable.grid(row=3,column=0)

    semesterlable=Label(addroot,text="Semester:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    semesterlable.grid(row=4,column=0)

    detainedlable=Label(addroot,text="Detained:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    detainedlable.grid(row=5,column=0)

    mobilelable=Label(addroot,text="Mobile No:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelable.grid(row=6,column=0)

    genderlable=Label(addroot,text="Gender:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlable.grid(row=7,column=0)

    parents_name=Label(addroot,text="Parent's Name:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    parents_name.grid(row=8,column=0)

    parents_no=Label(addroot,text="Parent's No:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    parents_no.grid(row=9,column=0)

    emailable=Label(addroot,text="Email-Id:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emailable.grid(row=10,column=0)

    adharlable=Label(addroot,text="Aadhar No:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    adharlable.grid(row=11,column=0)

    abcidlable=Label(addroot,text="ABC ID:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    abcidlable.grid(row=12,column=0)

    categorylable=Label(addroot,text="Category:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    categorylable.grid(row=13,column=0)  

    phlable=Label(addroot,text="Physical-H.:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    phlable.grid(row=14,column=0)

    #per==permanent address,pre==present address-----------------------------

    percitylable=Label(addroot,text="Per. City:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    percitylable.grid(row=15,column=0)
    
    perdistrictlable=Label(addroot,text="Per. District:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    perdistrictlable.grid(row=16,column=0)  

    perpinlable=Label(addroot,text="Per. Pincode:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    perpinlable.grid(row=17,column=0)

    precitylable=Label(addroot,text="Pre. City:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    precitylable.grid(row=0,column=3)

    predistrictlable=Label(addroot,text="Pre. District:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    predistrictlable.grid(row=1,column=3)

    prepinlable=Label(addroot,text="Pre. pincode:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    prepinlable.grid(row=2,column=3)

    cpilable=Label(addroot,text="CPI til date:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    cpilable.grid(row=3,column=3)

    spilable=Label(addroot,text="SPI of P. SEM.:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    spilable.grid(row=4,column=3)

    ssc_year_lable=Label(addroot,text="SSC passing Y.:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    ssc_year_lable.grid(row=5,column=3)  

    ssc_per_lable=Label(addroot,text="SSC-%:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    ssc_per_lable.grid(row=6,column=3)

    hsc_year_lable=Label(addroot,text="HSC passing Y.:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    hsc_year_lable.grid(row=7,column=3)  

    hsc_per_lable=Label(addroot,text="HSC-%:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    hsc_per_lable.grid(row=8,column=3)

    iti_year_lable=Label(addroot,text="ITI passing Y.:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    iti_year_lable.grid(row=9,column=3)

    iti_per_lable=Label(addroot,text="ITI-%:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    iti_per_lable.grid(row=10,column=3)

    #==================SEARCH STUDENT ENTRY==================#
    branchval= StringVar()
    enrollnoval= StringVar()
    nameval= StringVar()
    dobval= StringVar()
    semesterval= StringVar()
    detainedval= StringVar()
    mobileval= StringVar()
    genderval= StringVar()
    parents_nameval= StringVar()
    parents_noval= StringVar()
    emailval= StringVar()
    adharval= StringVar()   
    abcidval= StringVar()
    categoryval= StringVar()
    phval= StringVar()
    percityval= StringVar()
    perdistrictval= StringVar()
    perpinval= StringVar()
    precityval= StringVar()
    predistictval= StringVar()
    prepinval= StringVar()
    cpival= StringVar()
    spival= StringVar()
    ssc_yr_val= StringVar()
    ssc_per_val= StringVar()
    hsc_yr_val= StringVar()
    hsc_per_val= StringVar()
    iti_yr_val= StringVar()
    iti_per_val= StringVar()
#==================================================entry====================================================


    branchentry = ttk.Combobox(addroot, font=('times', 15, 'bold'), textvariable=branchval)
    branchentry['values'] = ['I.C.T','E.C']  # Add your branches here
    branchentry.grid(row=0, column=1)

    enrollnoentry=Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=enrollnoval)
    enrollnoentry.grid(row=1,column=1)

    nameentry=Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=nameval)
    nameentry.grid(row=2,column=1)

    dobentry=Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=dobval)
    dobentry.grid(row=3,column=1)

    semesterentry=Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=semesterval)
    semesterentry.grid(row=4,column=1)

    detainedentry = ttk.Combobox(addroot, font=('times', 15, 'bold'), textvariable=detainedval)
    detainedentry['values'] = ['Yes', 'No']  # Define the options for detained status
    detainedentry.grid(row=5, column=1)
    
    mobileentry=Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.grid(row=6,column=1)
    

    genderentry=ttk.Combobox(addroot, font=('times', 15, 'bold'), textvariable=genderval)
    genderentry['values'] = ['Male', 'Female', 'Other']  # Define the gender here
    genderentry.grid(row=7,column=1)

    parentsnameentry=Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=parents_nameval)
    parentsnameentry.grid(row=8,column=1)

    parentsnoentry=Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=parents_noval)
    parentsnoentry.grid(row=9,column=1)

    emailentry=Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=emailval)
    emailentry.grid(row=10,column=1)

    adharentry=Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=adharval)
    adharentry.grid(row=11,column=1)

    abcidentry=Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=abcidval)
    abcidentry.grid(row=12,column=1)

    categoryentry = ttk.Combobox(addroot, font=('times', 15, 'bold'), textvariable=categoryval)
    categories = ['General', 'OBC', 'SC', 'ST','SEBC']  # Add your categories here
    categoryentry['values'] = categories
    categoryentry.grid(row=13, column=1)

    phentry = ttk.Combobox(addroot, font=('times', 15, 'bold'), textvariable=phval)
    phentry['values'] = ['YES','NO']  # Add your branches here
    phentry.grid(row=14, column=1)

    percityentry=Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=percityval)
    percityentry.grid(row=15,column=1)

    perdistictentry=Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=perdistrictval)
    perdistictentry.grid(row=16,column=1)

    perpinentry=Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=perpinval)
    perpinentry.grid(row=17,column=1)

    precityentry=Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=precityval)
    precityentry.grid(row=0,column=4)

    predistrictentry=Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=predistictval)
    predistrictentry.grid(row=1,column=4)

    prepinentry=Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=prepinval)
    prepinentry.grid(row=2,column=4)

    cpientry=Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=cpival)
    cpientry.grid(row=3,column=4)

    spientry=Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=spival)
    spientry.grid(row=4,column=4)

    ssc_yr_entry=Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=ssc_yr_val)
    ssc_yr_entry.grid(row=5,column=4)
    
    ssc_per_entry=Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=ssc_per_val)
    ssc_per_entry.grid(row=6,column=4)

    hsc_yr_entry=Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=hsc_yr_val)
    hsc_yr_entry.grid(row=7,column=4)
    
    hsc_per_entry=Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=hsc_per_val)
    hsc_per_entry.grid(row=8,column=4)

    iti_yr_entry=Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=iti_yr_val)
    iti_yr_entry.grid(row=9,column=4)
    
    iti_per_entry=Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=iti_per_val)
    iti_per_entry.grid(row=10,column=4)

#===============SUBMIT BUTTON==================#
    subbtn = Button(addroot,text="ADD",font=("roman",15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='lightyellow',command=submitadd)
    subbtn.grid(row=12,column=4)


    addroot.mainloop()
#-----------------------------------------------------------------------------------------------------------#


def searchstudent():    
    def submitadd():
        branch = branchval.get()
        enrollno = enrollnoval.get()
        name = nameval.get()
        dob = dobval.get()
        sem = semesterval.get()
        detained = detainedval.get()
        mobile = mobileval.get()
        gender = genderval.get()
        parents_name = parents_nameval.get()
        parents_no = parents_noval.get()
        email = emailval.get()
        adharno = adharval.get()   
        abcid = abcidval.get()
        category = categoryval.get()
        physicalhandi = phval.get()
        percity = percityval.get()
        perdistrict = perdistrictval.get()
        perpin = perpinval.get()
        precity = precityval.get()
        predistrict = predistictval.get()
        prepin = prepinval.get()
        cpi = cpival.get()
        spi = spival.get()
        sscyear = ssc_yr_val.get()
        sscpercentage = ssc_per_val.get()
        hscyear = hsc_yr_val.get()
        hscpercentage = hsc_per_val.get()
        itiyear = iti_yr_val.get()
        itipercentage = iti_per_val.get()


        if(branch !=''):
            strr = 'select * from ictstudent1 where branch=%s'
            mycursor.execute(strr,(branch))
            datas =mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25],i[26],i[27],i[28]] #total29 
                studenttable.insert('',END,values=vv)

        elif(enrollno !=''):
            strr = 'select * from ictstudent1 where enrollnumber=%s'
            mycursor.execute(strr,(enrollno))
            datas =mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28]]
                studenttable.insert('',END,values=vv)

        elif(name !=''):
            strr = 'select * from ictstudent1 where name=%s'
            mycursor.execute(strr,(name))
            datas =mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28]]
                studenttable.insert('',END,values=vv)
        elif(dob !=''):
            strr = 'select * from ictstudent1 where dob=%s'
            mycursor.execute(strr,(dob))
            datas =mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28]]
                studenttable.insert('',END,values=vv)

        elif(sem !=''):
            strr = 'select * from ictstudent1 where sem=%s'
            mycursor.execute(strr,(sem))
            datas =mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28]]
                studenttable.insert('', END, values=vv)
        elif(detained !=''):
            strr = 'select * from ictstudent1 where detained=%s'
            mycursor.execute(strr,(detained))
            datas =mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28]]
                studenttable.insert('', END, values=vv) 

        elif(mobile !=''):
            strr = 'select * from ictstudent1 where mobile=%s'
            mycursor.execute(strr,(mobile))
            datas =mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28]]
                studenttable.insert('', END, values=vv) 
        #you can add gender and all new field :

        elif(gender !=''):
            strr = 'select * from ictstudent1 where gender=%s'
            mycursor.execute(strr,(gender))
            datas =mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28]]
                studenttable.insert('', END, values=vv) 

        elif(parents_name !=''):
            strr = 'select * from ictstudent1 where parentsname=%s'
            mycursor.execute(strr,(parents_name))
            datas =mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28]]
                studenttable.insert('', END, values=vv) 

        elif(parents_no !=''):
            strr = 'select * from ictstudent1 where parentsno=%s'
            mycursor.execute(strr,(parents_no))
            datas =mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28]]
                studenttable.insert('', END, values=vv) 

        
        elif(email !=''):
            strr = 'select * from ictstudent1 where email=%s'
            mycursor.execute(strr,(email))
            datas =mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28]]
                studenttable.insert('', END, values=vv)  

        elif(adharno !=''):
            strr = 'select * from ictstudent1 where adharno=%s'
            mycursor.execute(strr,(adharno))
            datas =mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28]]
                studenttable.insert('', END, values=vv) 

        elif(abcid !=''):
            strr = 'select * from ictstudent1 where abcid=%s'
            mycursor.execute(strr,(abcid))
            datas =mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28]]
                studenttable.insert('', END, values=vv) 

        elif(category !=''):
            strr = 'select * from ictstudent1 where category=%s'
            mycursor.execute(strr,(category))
            datas =mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28]]
                studenttable.insert('', END, values=vv)

        elif( physicalhandi!=''):
            strr = 'select * from ictstudent1 where physicalhandi=%s'
            mycursor.execute(strr,(physicalhandi))
            datas =mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28]]
                studenttable.insert('', END, values=vv) 

        elif(percity !=''):
            strr = 'select * from ictstudent1 where percity=%s'
            mycursor.execute(strr,(percity))
            datas =mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28]]
                studenttable.insert('', END, values=vv)   

        elif(perdistrict !=''):
            strr = 'select * from ictstudent1 where perdistrict=%s'
            mycursor.execute(strr,(perdistrict))
            datas =mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28]]
                studenttable.insert('', END, values=vv) 

        elif(perpin !=''):
            strr = 'select * from ictstudent1 where perpin=%s'
            mycursor.execute(strr,(perpin))
            datas =mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28]]
                studenttable.insert('', END, values=vv) 

        elif(precity !=''):
            strr = 'select * from ictstudent1 where precity=%s'
            mycursor.execute(strr,(precity))
            datas =mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28]]
                studenttable.insert('', END, values=vv)

        elif(predistrict !=''):
            strr = 'select * from ictstudent1 where predistrict=%s'
            mycursor.execute(strr,(predistrict))
            datas =mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28]]
                studenttable.insert('', END, values=vv)

        elif(prepin !=''):
            strr = 'select * from ictstudent1 where prepin=%s'
            mycursor.execute(strr,(prepin))
            datas =mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28]]
                studenttable.insert('', END, values=vv)

        elif(cpi !=''):
            strr = 'select * from ictstudent1 where cpi=%s'
            mycursor.execute(strr,(cpi))
            datas =mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28]]
                studenttable.insert('', END, values=vv)

        elif(spi !=''):
            strr = 'select * from ictstudent1 where spi=%s'
            mycursor.execute(strr,(spi))
            datas =mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28]]
                studenttable.insert('', END, values=vv)

        elif(sscyear !=''):
            strr = 'select * from ictstudent1 where sscyear=%s'
            mycursor.execute(strr,(sscyear))
            datas =mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28]]
                studenttable.insert('', END, values=vv)

        elif(sscpercentage !=''):
            strr = 'select * from ictstudent1 where sscpercentage=%s'
            mycursor.execute(strr,(sscpercentage))
            datas =mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28]]
                studenttable.insert('', END, values=vv)

        elif(hscyear !=''):
            strr = 'select * from ictstudent1 where hscyear=%s'
            mycursor.execute(strr,(hscyear))
            datas =mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28]]
                studenttable.insert('', END, values=vv)

        elif(hscpercentage !=''):
            strr = 'select * from ictstudent1 where hscpercentage=%s'
            mycursor.execute(strr,(hscpercentage))
            datas =mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28]]
                studenttable.insert('', END, values=vv)

        elif(itiyear !=''):
            strr = 'select * from ictstudent1 where itiyear=%s'
            mycursor.execute(strr,(itiyear))
            datas =mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28]]
                studenttable.insert('', END, values=vv)

        elif(itipercentage !=''):
            strr = 'select * from ictstudent1 where itipercentage=%s'
            mycursor.execute(strr,(itipercentage))
            datas =mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28]]
                studenttable.insert('', END, values=vv)
     
    searchroot = Toplevel(master=entry_frame)
    searchroot.grab_set()
    searchroot.geometry("980x800+220+200")
    searchroot.title("student Mnagement system")
    searchroot.config(bg='red')
    searchroot.resizable(FALSE,FALSE)
#==================SEARCH SYSTEM LABELS=================#
    branchlable=Label(searchroot,text="Enter Branch:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    branchlable.grid(row=0,column=0)

    enrollnolable=Label(searchroot,text="Enrollment no:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    enrollnolable.grid(row=1,column=0)

    namelable=Label(searchroot,text="Name:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelable.grid(row=2,column=0)

    doblable=Label(searchroot,text="D.o.b:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblable.grid(row=3,column=0)

    semesterlable=Label(searchroot,text="Semester:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    semesterlable.grid(row=4,column=0)

    detainedlable=Label(searchroot,text="Detained:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    detainedlable.grid(row=5,column=0)

    mobilelable=Label(searchroot,text="Mobile No:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelable.grid(row=6,column=0)

    genderlable=Label(searchroot,text="Gender:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlable.grid(row=7,column=0)

    parents_name=Label(searchroot,text="Parent's Name:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    parents_name.grid(row=8,column=0)

    parents_no=Label(searchroot,text="Parent's No:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    parents_no.grid(row=9,column=0)

    emailable=Label(searchroot,text="Email-Id:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emailable.grid(row=10,column=0)

    adharlable=Label(searchroot,text="Aadhar No:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    adharlable.grid(row=11,column=0)

    abcidlable=Label(searchroot,text="ABC ID:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    abcidlable.grid(row=12,column=0)

    categorylable=Label(searchroot,text="Category:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    categorylable.grid(row=13,column=0)  

    phlable=Label(searchroot,text="Physical-H.:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    phlable.grid(row=14,column=0)

    #per==permanent address,pre==present address-----------------------------

    percitylable=Label(searchroot,text="Per. City:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    percitylable.grid(row=15,column=0)
    
    perdistrictlable=Label(searchroot,text="Per. District:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    perdistrictlable.grid(row=16,column=0)  

    perpinlable=Label(searchroot,text="Per. Pincode:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    perpinlable.grid(row=17,column=0)

    precitylable=Label(searchroot,text="Pre. City:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    precitylable.grid(row=0,column=3)

    predistrictlable=Label(searchroot,text="Pre. District:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    predistrictlable.grid(row=1,column=3)

    prepinlable=Label(searchroot,text="Pre. pincode:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    prepinlable.grid(row=2,column=3)

    cpilable=Label(searchroot,text="CPI til date:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    cpilable.grid(row=3,column=3)

    spilable=Label(searchroot,text="SPI of P. SEM.:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    spilable.grid(row=4,column=3)

    ssc_year_lable=Label(searchroot,text="SSC passing Y.:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    ssc_year_lable.grid(row=5,column=3)  

    ssc_per_lable=Label(searchroot,text="SSC-%:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    ssc_per_lable.grid(row=6,column=3)

    hsc_year_lable=Label(searchroot,text="HSC passing Y.:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    hsc_year_lable.grid(row=7,column=3)  

    hsc_per_lable=Label(searchroot,text="HSC-%:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    hsc_per_lable.grid(row=8,column=3)

    iti_year_lable=Label(searchroot,text="ITI passing Y.:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    iti_year_lable.grid(row=9,column=3)

    iti_per_lable=Label(searchroot,text="ITI-%:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    iti_per_lable.grid(row=10,column=3)

    #==================SEARCH STUDENT ENTRY==================#
    branchval= StringVar()
    enrollnoval= StringVar()
    nameval= StringVar()
    dobval= StringVar()
    semesterval= StringVar()
    detainedval= StringVar()
    mobileval= StringVar()
    genderval= StringVar()
    parents_nameval= StringVar()
    parents_noval= StringVar()
    emailval= StringVar()
    adharval= StringVar()   
    abcidval= StringVar()
    categoryval= StringVar()
    phval= StringVar()
    percityval= StringVar()
    perdistrictval= StringVar()
    perpinval= StringVar()
    precityval= StringVar()
    predistictval= StringVar()
    prepinval= StringVar()
    cpival= StringVar()
    spival= StringVar()
    ssc_yr_val= StringVar()
    ssc_per_val= StringVar()
    hsc_yr_val= StringVar()
    hsc_per_val= StringVar()
    iti_yr_val= StringVar()
    iti_per_val= StringVar()
#==================================================entry====================================================


    branchentry = ttk.Combobox(searchroot, font=('times', 15, 'bold'), textvariable=branchval)
    branchentry['values'] = ['I.C.T','E.C']  # Add your branches here
    branchentry.grid(row=0, column=1)

    enrollnoentry=Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=enrollnoval)
    enrollnoentry.grid(row=1,column=1)

    nameentry=Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=nameval)
    nameentry.grid(row=2,column=1)

    dobentry=Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=dobval)
    dobentry.grid(row=3,column=1)

    semesterentry=Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=semesterval)
    semesterentry.grid(row=4,column=1)

    detainedentry = ttk.Combobox(searchroot, font=('times', 15, 'bold'), textvariable=detainedval)
    detainedentry['values'] = ['Yes', 'No']  # Define the options for detained status
    detainedentry.grid(row=5, column=1)
    
    mobileentry=Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.grid(row=6,column=1)
    

    genderentry=ttk.Combobox(searchroot, font=('times', 15, 'bold'), textvariable=genderval)
    genderentry['values'] = ['Male', 'Female', 'Other']  # Define the gender here
    genderentry.grid(row=7,column=1)

    parentsnameentry=Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=parents_nameval)
    parentsnameentry.grid(row=8,column=1)

    parentsnoentry=Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=parents_noval)
    parentsnoentry.grid(row=9,column=1)

    emailentry=Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=emailval)
    emailentry.grid(row=10,column=1)

    adharentry=Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=adharval)
    adharentry.grid(row=11,column=1)

    abcidentry=Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=abcidval)
    abcidentry.grid(row=12,column=1)

    categoryentry = ttk.Combobox(searchroot, font=('times', 15, 'bold'), textvariable=categoryval)
    categories = ['General', 'OBC', 'SC', 'ST','SEBC']  # Add your categories here
    categoryentry['values'] = categories
    categoryentry.grid(row=13, column=1)

    phentry = ttk.Combobox(searchroot, font=('times', 15, 'bold'), textvariable=phval)
    phentry['values'] = ['YES','NO']  # Add your branches here
    phentry.grid(row=14, column=1)

    percityentry=Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=percityval)
    percityentry.grid(row=15,column=1)

    perdistictentry=Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=perdistrictval)
    perdistictentry.grid(row=16,column=1)

    perpinentry=Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=perpinval)
    perpinentry.grid(row=17,column=1)

    precityentry=Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=precityval)
    precityentry.grid(row=0,column=4)

    predistrictentry=Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=predistictval)
    predistrictentry.grid(row=1,column=4)

    prepinentry=Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=prepinval)
    prepinentry.grid(row=2,column=4)

    cpientry=Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=cpival)
    cpientry.grid(row=3,column=4)

    spientry=Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=spival)
    spientry.grid(row=4,column=4)

    ssc_yr_entry=Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=ssc_yr_val)
    ssc_yr_entry.grid(row=5,column=4)
    
    ssc_per_entry=Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=ssc_per_val)
    ssc_per_entry.grid(row=6,column=4)

    hsc_yr_entry=Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=hsc_yr_val)
    hsc_yr_entry.grid(row=7,column=4)
    
    hsc_per_entry=Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=hsc_per_val)
    hsc_per_entry.grid(row=8,column=4)

    iti_yr_entry=Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=iti_yr_val)
    iti_yr_entry.grid(row=9,column=4)
    
    iti_per_entry=Entry(searchroot,font=('times',15,'bold'),bd=5,textvariable=iti_per_val)
    iti_per_entry.grid(row=10,column=4)

#===============SUBMIT BUTTON==================#
    subbtn = Button(searchroot,text="SEARCH",font=("roman",15,'bold'),width=20,bd=5,activebackground='white',activeforeground='white',bg='lightyellow',command=submitadd)
    subbtn.grid(row=11,column=4)


    searchroot.mainloop()

#l-------------------delete function------------------#    
def deletestudent():
    # Prompt for database password
    password = simpledialog.askstring("Database Password", "Enter database password:", show='*')
    
    # Check if the user canceled the prompt
    if password is None:
        return  # Exit the function if canceled

    if password != 'ict124':    #you can change passcode here current passcode is 'ict124'
        messagebox.showerror("Error", "Incorrect password!")
        return
        # Exit if the password is incorrect   
    cc = studenttable.focus()
    content = studenttable.item(cc)#focus elment to delete ontable 
    pp = content ['values'][1]
    strr = 'delete from ictstudent1 where enrollnumber=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notifications','Enroll {} deleted successfully...'.format(pp))
    strr = 'select * from ictstudent1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28]]
            studenttable.insert('',END,values=vv)

#---------------------------------------------------#

#-------------update function -----------------#    
def updatestudent():
    # Prompt for database password
    password = simpledialog.askstring("Database Password", "Enter database password:", show='*')
    
    # Check if the user canceled the prompt
    if password is None:
        return  # Exit the function if canceled

    if password != 'ict124':    #you can change passcode here current passcode is 'ict124'
        messagebox.showerror("Error", "Incorrect password!")
        return
        # Exit if the password is incorrect 
    
    def update():
        branch = branchval.get()
        enrollno = enrollnoval.get()
        name = nameval.get()
        dob = dobval.get()
        sem = semesterval.get()
        detained = detainedval.get()
        mobile = mobileval.get()
        gender = genderval.get() 
        parents_name = parents_nameval.get()
        parents_no = parents_noval.get()
        email = emailval.get()
        adharno = adharval.get()   
        abcid = abcidval.get()
        category = categoryval.get()
        physicalhandi = phval.get()
        percity = percityval.get()
        perdistrict = perdistrictval.get()
        perpin = perpinval.get()
        precity = precityval.get()
        predistrict = predistictval.get()
        prepin = prepinval.get()
        cpi = cpival.get()
        spi = spival.get()
        sscyear = ssc_yr_val.get()
        sscpercentage = ssc_per_val.get()
        hscyear = hsc_yr_val.get()
        hscpercentage = hsc_per_val.get()
        itiyear = iti_yr_val.get()
        itipercentage = iti_per_val.get()
       
        strr = '''UPDATE ictstudent1 
                  SET branch=%s, name=%s, dob=%s, semester=%s, detained=%s, mobile=%s, gender=%s,parentsname=%s,parentsno=%s,email=%s, adharnumber=%s, abcid=%s, category=%s, 
                      physicalhandicape=%s, percity=%s, perdistrict=%s, perpincode=%s, precity=%s, predistrict=%s, prepincode=%s, 
                      cpi=%s, spi=%s, sscyear=%s, sscpercentage=%s, hscyear=%s, hscpercentage=%s, itiyear=%s, 
                      itipercentage=%s 
                  WHERE enrollnumber=%s'''
        mycursor.execute(strr,(branch,name, dob, sem, detained, mobile,gender,parents_name,parents_no,email, adharno, abcid, category, physicalhandi, 
                                percity, perdistrict, perpin, precity, predistrict, prepin, cpi, spi, sscyear, 
                                sscpercentage, hscyear, hscpercentage, itiyear, itipercentage, enrollno))
        
        con.commit()
        
        # Show success message
        messagebox.showinfo('Notification', 'Enrollno {} modified successfully...'.format(enrollno), parent=updateroot)
        
        # Fetch updated data from the database
        strr = 'SELECT * FROM ictstudent1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
    
    # Clear the existing rows in the student table
        studenttable.delete(*studenttable.get_children())  # Proper method to clear the table
    
    # Insert the updated data into the table
        for i in datas:
            vv = list(i)  # Convert tuple to list dynamically
            studenttable.insert('', 'end', values=vv)
     
    updateroot = Toplevel(master=entry_frame)
    updateroot.grab_set()
    updateroot.geometry("980x800+220+160")
    updateroot.title("student Mnagement system")
    updateroot.config(bg='lightgrey')
    updateroot.resizable(FALSE,FALSE)
#==================UPDATE SYSTEM LABELS=================#

    branchlable=Label(updateroot,text="Enter Branch:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    branchlable.grid(row=0,column=0)

    enrollnolable=Label(updateroot,text="Enrollment No:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    enrollnolable.grid(row=1,column=0)

    namelable=Label(updateroot,text="Name:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelable.grid(row=2,column=0)

    doblable=Label(updateroot,text="D.o.b dd/mm/yyyy:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblable.grid(row=3,column=0)

    semesterlable=Label(updateroot,text="Semester:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    semesterlable.grid(row=4,column=0)

    detainedlable=Label(updateroot,text="Detained:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    detainedlable.grid(row=5,column=0)

    mobilelable=Label(updateroot,text="Mobile No:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelable.grid(row=6,column=0)

    genderlable=Label(updateroot,text="Gender:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlable.grid(row=7,column=0)

    parents_name=Label(updateroot,text="Parent's Name:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    parents_name.grid(row=8,column=0)

    parents_no=Label(updateroot,text="Parent's No:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    parents_no.grid(row=9,column=0)

    emailable=Label(updateroot,text="Email-Id:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emailable.grid(row=10,column=0)

    adharlable=Label(updateroot,text="Aadhar No:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    adharlable.grid(row=11,column=0)

    abcidlable=Label(updateroot,text="ABC ID:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    abcidlable.grid(row=12,column=0)

    categorylable=Label(updateroot,text="Category:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    categorylable.grid(row=13,column=0)  

    phlable=Label(updateroot,text="Physical-H.:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    phlable.grid(row=14,column=0)

    #per==permanent address,pre==present address-----------------------------

    percitylable=Label(updateroot,text="Per. City:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    percitylable.grid(row=15,column=0)
    
    perdistrictlable=Label(updateroot,text="Per. District:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    perdistrictlable.grid(row=16,column=0)  

    perpinlable=Label(updateroot,text="Per. Pincode:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    perpinlable.grid(row=17,column=0)

    precitylable=Label(updateroot,text="Pre. City:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    precitylable.grid(row=18,column=0)

    predistrictlable=Label(updateroot,text="Pre. District:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    predistrictlable.grid(row=1,column=3)

    prepinlable=Label(updateroot,text="Pre. pincode:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    prepinlable.grid(row=2,column=3)

    cpilable=Label(updateroot,text="CPI til date:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    cpilable.grid(row=3,column=3)

    spilable=Label(updateroot,text="SPI of P. SEM.:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    spilable.grid(row=4,column=3)

    ssc_year_lable=Label(updateroot,text="SSC passing Y.:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    ssc_year_lable.grid(row=5,column=3)  

    ssc_per_lable=Label(updateroot,text="SSC-%:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    ssc_per_lable.grid(row=6,column=3)

    hsc_year_lable=Label(updateroot,text="HSC passing Y.:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    hsc_year_lable.grid(row=7,column=3)  

    hsc_per_lable=Label(updateroot,text="HSC-%:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    hsc_per_lable.grid(row=8,column=3)

    iti_year_lable=Label(updateroot,text="ITI passing Y.:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    iti_year_lable.grid(row=9,column=3)

    iti_per_lable=Label(updateroot,text="ITI-%:",bg="gold2",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    iti_per_lable.grid(row=10,column=3)




    #==================ADD STUDENT ENTRY==================#
    branchval= StringVar()
    enrollnoval= StringVar()
    nameval= StringVar()
    dobval= StringVar()
    semesterval= StringVar()
    detainedval= StringVar()
    mobileval= StringVar()
    genderval = StringVar()
    parents_nameval = StringVar()
    parents_noval = StringVar()
    emailval= StringVar()
    adharval= StringVar()   
    abcidval= StringVar()
    categoryval= StringVar()
    phval= StringVar()
    percityval= StringVar()
    perdistrictval= StringVar()
    perpinval= StringVar()
    precityval= StringVar()
    predistictval= StringVar()
    prepinval= StringVar()
    cpival= StringVar()
    spival= StringVar()
    ssc_yr_val= StringVar()
    ssc_per_val= StringVar()
    hsc_yr_val= StringVar()
    hsc_per_val= StringVar()
    iti_yr_val= StringVar()
    iti_per_val= StringVar()

   #-------------------------------------enrtry data-------------------------------------

    branchentry = ttk.Combobox(updateroot, font=('times', 15, 'bold'), textvariable=branchval)
    branchentry['values'] = ['I.C.T','E.C']  # Add your branches here
    branchentry.grid(row=0, column=1)

    enrollnoentry=Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=enrollnoval)
    enrollnoentry.grid(row=1,column=1)

    nameentry=Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=nameval)
    nameentry.grid(row=2,column=1)

    dobentry=Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=dobval)
    dobentry.grid(row=3,column=1)

    semesterentry=Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=semesterval)
    semesterentry.grid(row=4,column=1)

    detainedentry = ttk.Combobox(updateroot, font=('times', 15, 'bold'), textvariable=detainedval)
    detainedentry['values'] = ['Yes', 'No']  # Define the options for detained status
    detainedentry.grid(row=5, column=1)

    mobileentry=Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.grid(row=6,column=1)

    genderentry=ttk.Combobox(updateroot, font=('times', 15, 'bold'), textvariable=genderval)
    genderentry['values'] = ['Male', 'Female', 'Other']  # Define the gender here
    genderentry.grid(row=7,column=1)

    parentsnameentry=Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=parents_nameval)
    parentsnameentry.grid(row=8,column=1)

    parentsnoentry=Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=parents_noval)
    parentsnoentry.grid(row=9,column=1)

    emailentry=Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=emailval)
    emailentry.grid(row=10,column=1)

    adharentry=Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=adharval)
    adharentry.grid(row=11,column=1)

    abcidentry=Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=abcidval)
    abcidentry.grid(row=12,column=1)

    categoryentry = ttk.Combobox(updateroot, font=('times', 15, 'bold'), textvariable=categoryval)
    categories = ['General', 'OBC', 'SC', 'ST','SEBC']  # Add your categories here
    categoryentry['values'] = categories
    categoryentry.grid(row=13, column=1)

    phentry = ttk.Combobox(updateroot, font=('times', 15, 'bold'), textvariable=phval)
    phentry['values'] = ['YES','NO']  # Add your branches here
    phentry.grid(row=14, column=1)


    percityentry=Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=percityval)
    percityentry.grid(row=15,column=1)

    perdistictentry=Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=perdistrictval)
    perdistictentry.grid(row=16,column=1)

    perpinentry=Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=perpinval)
    perpinentry.grid(row=17,column=1)

    precityentry=Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=precityval)
    precityentry.grid(row=18,column=1)

    predistrictentry=Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=predistictval)
    predistrictentry.grid(row=1,column=4)

    prepinentry=Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=prepinval)
    prepinentry.grid(row=2,column=4)

    cpientry=Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=cpival)
    cpientry.grid(row=3,column=4)

    spientry=Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=spival)
    spientry.grid(row=4,column=4)

    ssc_yr_entry=Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=ssc_yr_val)
    ssc_yr_entry.grid(row=5,column=4)
    
    ssc_per_entry=Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=ssc_per_val)
    ssc_per_entry.grid(row=6,column=4)

    hsc_yr_entry=Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=hsc_yr_val)
    hsc_yr_entry.grid(row=7,column=4)
    
    hsc_per_entry=Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=hsc_per_val)
    hsc_per_entry.grid(row=8,column=4)

    iti_yr_entry=Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=iti_yr_val)
    iti_yr_entry.grid(row=9,column=4)
    
    iti_per_entry=Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=iti_per_val)
    iti_per_entry.grid(row=10,column=4)

#===============SUBMIT BUTTON==================#
    subbtn = Button(updateroot,text="UPDATE",font=("roman",15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='blue',command=update,bg='red')
    subbtn.grid(row=15,column=4)
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if(len(pp) != 0):
            branchval.set(pp[0])
            enrollnoval.set(pp[1])
            nameval.set(pp[2])
            dobval.set(pp[3])
            semesterval.set(pp[4])
            detainedval.set(pp[5])
            mobileval.set(pp[6])
            genderval.set(pp[7])
            parents_nameval.set(pp[8])
            parents_noval.set(pp[9])
            emailval.set(pp[10])
            adharval.set(pp[11])   
            abcidval.set(pp[12])
            categoryval.set(pp[13])
            phval.set(pp[14])
            percityval.set(pp[15])
            perdistrictval.set(pp[16])
            perpinval.set(pp[17])
            precityval.set(pp[18])
            predistictval.set(pp[19])
            prepinval.set(pp[20])
            cpival.set(pp[21])
            spival.set(pp[22])
            ssc_yr_val.set(pp[23])
            ssc_per_val.set(pp[24])
            hsc_yr_val.set(pp[25])
            hsc_per_val.set(pp[26])
            iti_yr_val.set(pp[27])
            iti_per_val.set(pp[28])


    updateroot.mainloop()
#------------------------------------------------------------------------------#

#----------------------show detail---------------#
   
def showstudent():
    strr ='select * from  ictstudent1'
    mycursor.execute(strr)
    datas =mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25],i[26],i[27],i[28]]
        studenttable.insert('',END,values=vv)



#-----------------------------------------------------------------#

#----------------------export detail----------------------
def exportstudent():
    ff= filedialog.asksaveasfilename()
    gg= studenttable.get_children()
    branch,enrollno,name,dob,semester,detained,mobile,gender,parentsname,parentsno,adhar,email,abcid,category,ph,percity,perdistrict,perpin,precity,predistict,prepin,cpi,spi,ssc_yr,ssc_per,hsc_yr,hsc_per,iti_yr,iti_per=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]# 29
    for i in gg:
        content=studenttable.item(i)
        pp = content['values']
        enrollno.append(pp[1]),branch.append(pp[0]),name.append(pp[2]),dob.append(pp[3]),semester.append(pp[4]),detained.append(pp[5]),mobile.append(pp[6]),gender.append(pp[7]),parentsname.append(pp[8]),parentsno.append(pp[9]),adhar.append(pp[10]),email.append(pp[11]),abcid.append(pp[12]),category.append(pp[13]),ph.append(pp[14]),percity.append(pp[15]),perdistrict.append(pp[16]),perpin.append(pp[17]),precity.append(pp[18]),predistict.append(pp[19]),prepin.append(pp[20]),spi.append(pp[21]),cpi.append(pp[22]),ssc_yr.append(pp[23]),ssc_per.append(pp[24]),hsc_yr.append(pp[25]),hsc_per.append(pp[26]),iti_yr.append(pp[27]),iti_per.append(pp[28])
    dd=['branch','enrollno','name','dob','semester','detained','mobile','gender','parentsname','parentsno','adhar','email','abcid','category','ph','percity','perdistrict','perpin','precity','predistict','prepin','cpi','spi','ssc_yr','ssc_per','hsc_yr','hsc_per','iti_yr','iti_per']
    df= pandas.DataFrame(list(zip(branch,enrollno,name,dob,semester,detained,gender,parentsname,parentsno,mobile,adhar,email,abcid,category,ph,percity,perdistrict,perpin,precity,predistict,prepin,cpi,spi,ssc_yr,ssc_per,hsc_yr,hsc_per,iti_yr,iti_per)),columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths,index=FALSE)
    messagebox.showinfo('Notification', 'Student data is saved {} successfully...'.format(paths))

#------exit---------------------

def exitstudent():
    res = messagebox.askyesnocancel('notification','do you want to exit?')
    if(res==True):
        root.destroy()

#=========Conncetion to Database===========#
def connectdb():
    def submitdb():
       global con,mycursor
       host = hostval.get()
       user= userval.get()
       password= passwordval.get()                 
       try:
          con = pymysql.connect(host=host,user=user,password=password)
          mycursor = con.cursor()
       except:
          messagebox.showerror('Notification',' Data is incorrect') 
          return
       try:
          strr = 'create database ict24'
          mycursor.execute(strr)
          strr = 'use ict24'
          mycursor.execute(strr)
          strr = 'create table ictstudent1(branch varchar(10),enrollnumber varchar(12),name varchar(100),dob varchar(50),semester varchar(25),detained varchar(25),mobile varchar(20),gender varchar(15),parentsname varchar(90),parentsno varchar(10),email varchar(250),adharnumber varchar(50),abcid varchar(50),category varchar(50),physicalhandicape varchar(250),percity varchar(250),perdistrict varchar(250),perpincode varchar(10),precity varchar(250),predistrict varchar(250),prepincode varchar(10),cpi varchar(20),spi varchar(20),sscyear varchar(25),sscpercentage varchar(25),hscyear varchar(25),hscpercentage varchar(25),itiyear varchar(25),itipercentage varchar(25))'
          mycursor.execute(strr)
          strr = 'alter table ictstudent1 modify enrollnumber varchar(12) not null'
          mycursor.execute(strr)
          strr = 'alter table ictstudent1 modify column enrollnumber varchar(12) primary  key'
          mycursor.execute(strr)        
          messagebox.showinfo('Notification','database created and now you are connected to database....',parent=dbroot)
       except:
          strr = 'use ict24'
          mycursor.execute(strr)          
          messagebox.showinfo('Notification',' you are connected to database....',parent=dbroot)
          dbroot.destroy()
         #=============================#           
    dbroot= Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.resizable(False,False)
    dbroot.config(bg='blue')
     #====connect Lables========#  
    hostlabel= Label(dbroot,text="Enter Host :",bg='gold2',font=('times', 20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel= Label(dbroot,text="Enter User  :",bg='gold2',font=('times', 20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    userlabel.place(x=10,y=70)

    passwordlabel= Label(dbroot,text="Enter Password:",bg='gold2',font=('times', 20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    passwordlabel.place(x=10,y=130)

    #===========Connectdb entry=============#
    hostval=StringVar()
    userval=StringVar()
    passwordval=StringVar()
    hostentry= Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userentry= Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=userval)
    userentry.place(x=250,y=70)

    passwordentry= Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=passwordval,show='*')
    passwordentry.place(x=250,y=130)

    #=============Connectdb button=========#
    submitbutton = Button(dbroot,text='Submit',font=('roman',15,'bold'),bg='red',bd=5,width=20,activebackground='blue',activeforeground='white',command= submitdb)
    submitbutton.place(x=150,y=190)
    dbroot.mainloop()

#=========================================#
#=========================================#
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    #print(time_string,date_string)
    clk.config(text='Date:'+date_string+"\n"+"Time:-"+time_string)
    clk.after(200,tick)
#===================================#
#=========INTRO SLIDDER=======#
import random
colors = ['red','green','blue','yellow','pink','red2','gold2']
def IntroLableColorTick():
    fg = random.choice(colors)
    sliderlabel.config(fg=fg)
    sliderlabel.after(2,IntroLableColorTick)
def introlabeltick():
    global count,text
    if(count>= len(ss)):
        count = 0  # Reset count to 0 instead of -1
        text = ""
        sliderlabel.config(text=text)
    else:
        text = text+ss[count]
        sliderlabel.config(text=text)
        count+=1
    sliderlabel.after(200,introlabeltick)  # Calls itself after 200ms
#=====================================main display program==============================================================================#
# Import necessary modules from tkinter
from tkinter import *
from tkinter import Toplevel,messagebox,filedialog,simpledialog
from tkinter.ttk import Treeview
from tkinter import ttk
import time
import pymysql 
import pandas
# Initialize the main window
root = Tk()
root.title("I.C.T Student Management System")
root.config(bg='gold2')

# Set window geometry and disable resizing
root.geometry('1174x700+200+50')
root.resizable(False, False)

# -------------FRAME SECTION-----------------

# Frame for entry section
entry_frame = Frame(root, bg="gold2", relief=GROOVE, borderwidth=5)
entry_frame.place(x=10, y=80, width=500, height=600)

##----------------------------------------------------------------------------------------------------data entry-------------------##
frontlable = Label(entry_frame,text="----------welcome-----------",width=30,font=('arial',22,'italic bold'),bg="gold2")
frontlable.pack(side=TOP,expand=TRUE)

addbtn = Button(entry_frame,text='1.Add student',width=25,font=("chiler",20,'bold'),bd=6,bg="skyblue3",activebackground='blue',relief=RIDGE,activeforeground='white',command=addstudeent)
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(entry_frame,text='2.Search student',width=25,font=("chiler",20,'bold'),bd=6,bg="skyblue3",activebackground='blue',relief=RIDGE,activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

deletebtn = Button(entry_frame,text='3.Delete student',width=25,font=("chiler",20,'bold'),bd=6,bg="skyblue3",activebackground='blue',relief=RIDGE,activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

updatebtn = Button(entry_frame,text='4.Update student',width=25,font=("chiler",20,'bold'),bd=6,bg="skyblue3",activebackground='blue',relief=RIDGE,activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showbtn = Button(entry_frame,text='5.Show all ',width=25,font=("chiler",20,'bold'),bd=6,bg="skyblue3",activebackground='blue',relief=RIDGE,activeforeground='white',command=showstudent)
showbtn.pack(side=TOP,expand=True)

exportbtn = Button(entry_frame,text='6.Export data',width=25,font=("chiler",20,'bold'),bd=6,bg="skyblue3",activebackground='blue',relief=RIDGE,activeforeground='white',command=exportstudent)
exportbtn.pack(side=TOP,expand=True)

exitbtn = Button(entry_frame,text='7.Exit',width=25,font=("chiler",20,'bold'),bd=6,bg="skyblue3",activebackground='blue',relief=RIDGE,activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)

# Frame for display section
dis_entry_frame = Frame(root, bg='gold2', relief=GROOVE, borderwidth=5)
dis_entry_frame.place(x=550, y=80, width=620, height=600)
style= ttk.Style()
style.configure('Treeview.Heading',font=('Roman',16,'bold'),foreground='blue')
style.configure('Treeview',font=('times',15,'bold'),foreground='black',background='lightpink')

#===============Scroll Bar ===========#
Scroll_x= Scrollbar(dis_entry_frame,orient=HORIZONTAL)
Scroll_y= Scrollbar(dis_entry_frame,orient=VERTICAL)
studenttable = Treeview(dis_entry_frame,columns=('Branch','Enrollment-No','Name','D.O.B','Semester','Detained','Mobile No.','Gender','Parents-Name','Parents-No','Email id','Adhar No','ABC ID','Category','Physical-Handicape','Permanent-City','Permanent-Distict','Permanent-Pincode','Present-City','Present-District','Present-Pincode','C.P.I','S.P.I','SSC-Year','SSC-per%','HSC-Year','HSC-per%','I.T.I-Year','I.T.I-per%'),yscrollcommand=Scroll_y.set,xscrollcommand=Scroll_x.set)
Scroll_x.pack(side=BOTTOM,fill=X)
Scroll_y.pack(side=RIGHT,fill=Y)
Scroll_x.config(command=studenttable.xview)
Scroll_y.config(command=studenttable.yview)
#==========this code is to show Headings  in Output panel=====# 
studenttable.heading('Branch',text='Branch')
studenttable.heading('Enrollment-No',text='Enrollment-No')
studenttable.heading('Name',text='Name')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Semester',text='Semester')
studenttable.heading('Detained',text='Detained')
studenttable.heading('Mobile No.',text='Mobile No.')
studenttable.heading('Gender',text='Gender')
studenttable.heading('Parents-Name',text='Parents-Name')
studenttable.heading('Parents-No',text='Parents-No')
studenttable.heading('Email id',text='Email ID')
studenttable.heading('Adhar No',text='Adhar No.')
studenttable.heading('ABC ID',text='ABC ID')
studenttable.heading('Category',text='Category')
studenttable.heading('Physical-Handicape',text='Physical-Handicape')
studenttable.heading('Permanent-City',text='Permanent-City')
studenttable.heading('Permanent-Distict',text='Permanent-Distict')
studenttable.heading('Permanent-Pincode',text='Permanent-Pincode')
studenttable.heading('Present-City',text='Present-City')
studenttable.heading('Present-District',text='Present-District')
studenttable.heading('Present-Pincode',text='Present-Pincode')
studenttable.heading('C.P.I',text='C.P.I')
studenttable.heading('S.P.I',text='S.P.I')
studenttable.heading('SSC-Year',text='SSC-Year')
studenttable.heading('SSC-per%',text='SSC-per%')
studenttable.heading('HSC-Year',text='HSC-Year')
studenttable.heading('HSC-per%',text='HSC-per%')
studenttable.heading('I.T.I-Year',text='I.T.I-Year')
studenttable.heading('I.T.I-per%',text='I.T.I-per%')
studenttable.pack(fill=BOTH,expand=1)

studenttable['show']='headings'

#========= below Code changes the size  of each row to the users need===#
studenttable.column('Branch',width=150)
studenttable.column('Enrollment-No',width=200)
studenttable.column('Name',width=200)
studenttable.column('D.O.B',width=150)
studenttable.column('Semester',width=150)
studenttable.column('Detained',width=150)
studenttable.column('Mobile No.',width=200)
studenttable.column('Gender',width=200)
studenttable.column('Parents-Name',width=200)
studenttable.column('Parents-No',width=200)
studenttable.column('Email id',width=400)
studenttable.column('Adhar No',width=150)
studenttable.column('ABC ID',width=150)
studenttable.column('Category',width=150)
studenttable.column('Physical-Handicape',width=200)
studenttable.column('Permanent-City',width=200)
studenttable.column('Permanent-Distict',width=200)
studenttable.column('Permanent-Pincode',width=200)
studenttable.column('Present-City',width=200)
studenttable.column('Present-District',width=200)
studenttable.column('Present-Pincode',width=200)
studenttable.column('C.P.I',width=150)
studenttable.column('S.P.I',width=150)
studenttable.column('SSC-Year',width=150)
studenttable.column('SSC-per%',width=150)
studenttable.column('HSC-Year',width=150)
studenttable.column('HSC-per%',width=150)
studenttable.column('I.T.I-Year',width=150)
studenttable.column('I.T.I-per%',width=150)

# ---------SLIDER SECTION---------

# Text to be displayed in the slider
ss = 'Welcome to I.C.T Database Management System'
count = 0
text = ""

# Slider label to display welcome message
sliderlabel = Label(root, text=ss, relief=RIDGE, borderwidth=4, font=('chiller', 25, 'italic bold'), width=50,bg='cyan')
sliderlabel.place(x=260, y=15)
introlabeltick()  # Start the sliding text animation
IntroLableColorTick() # call Random Lable Color 

# Clock label (currently not showing the time)
clk = Label(root, font=('times', 14, 'bold'), relief=RIDGE, borderwidth=4, bg='lawn green')
clk.place(x=0, y=0)
tick()
#=========================Connect DataBase Button=================================#
connectbutton= Button(root,text="Connect To DataBase",width=23,font=('Roman', 17, 'italic bold'),relief=RIDGE,bd=4,bg='green2',activebackground='blue',activeforeground='white',command=connectdb)
connectbutton.place(x=930,y=0)


# Start the main loop
root.mainloop()