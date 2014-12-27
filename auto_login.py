import sys
import mechanize


# Logins to filmai.in with user credentials.
def auto_login(user, password):
	browser = mechanize.Browser()
	browser.open('http://filmai.in')
	browser.select_form(nr = 0)
	browser['login_name'] = user
	browser['login_password'] = password
	browser.submit('image')


def main(args = None):
	if len(args) < 3:
		print("Bad parameters.")
		exit(-1)

	auto_login(args[1], args[2])


if __name__ == "__main__":
	main(sys.argv)
