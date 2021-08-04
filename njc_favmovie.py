import sqlite3
sql_connection = sqlite3.connect('movie_db.db')
print('Database Created successfully')
cr = sql_connection.cursor()
cr.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='movies' ''')
if cr.fetchone()[0]==1 : {
    print('Table exists.')
}
else:
    print('No Table Found')
    print("Creating Table.....")
#Create Table Statement
    cr.execute("create table movies(movie_name text, actor_name text, actress_name text, director_name text, year_of_release text)")

#Insert Values To Tables
    cr.execute("insert into movies values('Avengers Endgame','robert downey jr','scarlette johansson','joe russo','2019')")
    cr.execute("insert into movies values('3-Idiots','amir khan','kareena kapoor','rajkumar hirani','2009')")
    cr.execute("insert into movies values('Ham Apke Hai Kon','salman khan','madhuri dixit','sooraj barjatya','1994')")
    cr.execute("insert into movies values('Jindagi Na Milegi Dobara','hrithik roshan','katrina kaif','zoya akhtar','2011')")
    cr.execute("insert into movies values('Partner','govinda','katrina kaif','david dhawan','2007')")
    cr.execute("insert into movies values('Lage Raho Munna Bhai','sanjay dutt','vidhya balan','rajkumar hirani','2006')")
    sql_connection.commit()
    print('Table Updated Succesfully')
sql_connection.commit()
print('Database Updated Succesfully')
cursor = sql_connection.execute("SELECT movie_name,actor_name,actress_name,director_name,year_of_release from movies")
for row in cursor:
    print("\n")
    print("Movie=",row[0])
    print("Actor = ", row[1])
    print("Actress = ", row[2])
    print("Director = ", row[3])
    print("Year_of_release = ", row[4], "\n")
flag=1
while flag==1:
    a = input("Enter your choice from the following:\n1-> Actor\n2-> Actress\n3-> Director\nYour Choice:")
    if a == '1':
        no=1
        print('Select any name:\n')
        actor = sql_connection.execute("SELECT DISTINCT actor_name from movies order by actor_name ASC")
        for actor_names in actor:
            print(f'{no}->{actor_names[0]}')
            no += 1
        b = input('Enter your actor choice:')
        if b == '1':
            i=cr.execute("select * from movies where actor_name='amir khan'")
        elif b == '2':
            i=cr.execute("select * from movies where actor_name='govinda'")
        elif b == '3':
            i=cr.execute("select * from movies where actor_name='hrithik roshan'")
        elif b == '4':
            i=cr.execute("select * from movies where actor_name='robert downey jr'")
        elif b == '5':
            i=cr.execute("select * from movies where actor_name='salman khan'")
        elif b == '6':
            i=cr.execute("select * from movies where actor_name='sanjay dutt'")
        else:
            print('Wrong Input')
            continue
        print("\6 "*25)
        print("\5 "*25)
        print("Your fav Movie:",end=' ')
        for data in i:
            print(data[0],end=', ')
        print("\n"+"\5 "*25)
        print("\6 "*25)
    elif a == '2':
        no = 1
        print('Select any name:\n')
        actress = sql_connection.execute("SELECT DISTINCT actress_name from movies order by actress_name ASC")
        for actress_names in actress:
            print(f'{no}->{actress_names[0]}')
            no += 1
        c = input('Enter your actress choice:')
        if c == '1':
            j=cr.execute("select * from movies where actress_name='kareena kapoor'")
        elif c == '2':
            j=cr.execute("select * from movies where actress_name='katrina kaif'")
        elif c == '3':
            j=cr.execute("select * from movies where actress_name='madhuri dixit'")
        elif c == '4':
            j=cr.execute("select * from movies where actress_name='scarlette johansson'")
        elif c == '5':
            j=cr.execute("select * from movies where actress_name='vidhya balan'")
        else:
            print('Wrong Input')
            continue
        print("\6 "*25)
        print("\5 "*25)
        print("Your fav Movie:",end=' ')
        for data in j:
            print(data[0],end=', ' )
        print("\n"+"\5"*25)
        print("\6 "*25)
    elif a =='3':
        no =1
        print('Select any name:\n')
        director = sql_connection.execute("SELECT DISTINCT director_name from movies order by director_name ASC")
        for director_names in director:
            print(f'{no}->{director_names[0]}')
            no += 1
        d = input('Enter your actor choice:')
        if d == '1':
            k=cr.execute("select * from movies where director_name='david dhawan'")
        elif d == '2':
            k=cr.execute("select * from movies where director_name='joe russo'")
        elif d == '3':
            k=cr.execute("select * from movies where director_name='rajkumar hirani'")
        elif d == '4':
            k=cr.execute("select * from movies where director_name='sooraj barjatya'")
        elif d == '5':
            k=cr.execute("select * from movies where director_name='zoya akhtar'")
        else:
            print('Wrong Input')
            continue
        print("\6 "*25)
        print("\5 "*25)
        print("Your fav Movie :",end=' ')
        for data in k:
            print(data[0],end=', ')
        print("\n"+"\5 "*25)
        print("\6 "*25)
    else:
        print('Wrong Input')
        continue
    con = input('Do you want to continue(Y/N)').lower()
    if con == 'y':
        flag == 1
    elif con == 'n':
        flag == 0
        print('See you again!!')
        break
    continue
sql_connection.close()