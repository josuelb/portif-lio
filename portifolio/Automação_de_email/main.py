import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def enviar_email(to):
    host = "smtp.office365.com"
    port = "587"
    login = 'jlb.silva1243@hotmail.com'
    password = 'Arrebatamento2#070504joshua'

    #Start no server
    server = smtplib.SMTP(host, port)
    server.ehlo()
    server.starttls()

    server.login(login, password)

    #Criação do email
    corpo = """
    <p>Prezado,</p>
    <p>Esse email é automático, não é preciso respondelo</p>
    <p>Venho relatar que seu comentario no post do portifólio de Josue Luiz B. Silva foi recebido com sucesso, breve estaremos analisando-o e, no caso de perguntas, respondendo-o.
    <p>Obrigado pela a participação!!!</p> 
    """
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = to
    email_msg['Subject'] = "Seu comentario foi enviado e recebido-JLB.Silva"
    email_msg.attach(MIMEText(corpo, 'html'))

    #enviar o email
    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())

    print(f'Email enviado para {to}')

    server.quit()
