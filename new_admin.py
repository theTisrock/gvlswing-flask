import smtplib


def test_send_mail():
	with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()
		smtp.login(email, password)

		subject = "here is a subject"
		body = "here is the body"

		message = f'Subject: {subject}\n\n{body}'

		smtp.sendmail(source_email, source_password, message)

