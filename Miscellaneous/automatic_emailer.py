# Problem in login/password section...

import smtplib

# add 'cc_addr_list' to args in function definition
# add 'cc_addr_list = ['RC@xx.co.uk']' in function call

def sendemail(from_addr, to_addr_list, 
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    # header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems
	
	
sendemail(from_addr    = 'swebert@live.com', 
          to_addr_list = ['genius.sbt.1920@gmail.com'], 
          subject      = 'Howdy', 
          message      = 'Howdy from a python function', 
          login        = 'swebert@live.com', 
          password     = 'player007')
