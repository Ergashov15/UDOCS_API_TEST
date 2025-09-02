from servises.Authentication.model_authentication.model_authentication import ResponseAuthModel


class AuthenticationEndpoint:

    ENDPOINT= "/client"
    #AUTH_LOGIN =f"{ENDPOINT}/auth/login"
    @staticmethod
    def auth_login_end(username_, password_):
        return "/client/auth/login?username={}&password={}".format(username_, password_)