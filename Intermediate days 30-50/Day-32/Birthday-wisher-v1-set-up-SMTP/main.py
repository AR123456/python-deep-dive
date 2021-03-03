import smtplib

connection =smtplib.SMTP()
my_email= "test@test.com"
password = "testing123"
#open and close the connection
with smtplib.SMTP("smtp.test.com") as connection:
    #this line encripts prior to sending
    connection.starttls()
    #login
    connection.login(user=my_email, password=password)
    # send email
    connection.sendmail(from_addr=my_email,
                        to_addres = "testToo@test.com",
                        msg="Subject: Hello\n\nThis is the body of teh email",)


