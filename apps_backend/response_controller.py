# used for controlling the responses
# that gets generated in case
# if something goes wrong


from flask import jsonify


class Error :

    #CODE
    BAD_REQUEST_CODE = 400
    UNAUTHOIRZED_CODE = 401
    CONTENT_NOT_FOUND_CODE = 404
    REQUEST_FORBIDDEN = 403
    CONFLICT_CODE = 409
    UNSUPPORTED_MEDIA_TYPE_CODE = 415

    #STATUS
    BAD_REQUEST_STATUS = "BAD_REQUEST"
    UNAUTHORIZED_STATUS = "PERMISSION_DENIED"
    CONTENT_NOT_FOUND_STATUS = "CONTENT_NOT_FOUND"
    REQUEST_FORBIDDEN_STATUS = "REQUEST_FORBIDDEN"
    CONFLICT_STATUS = "CONFLICT"
    UNSUPPORTED_MEDIA_TYPE_STATUS = "UNSUPPORTED_MEDIA_TYPE"

    #MESSAGE
    BAD_REQUEST_MESSAGE = "Arguments are not valid."
    UNAUTHORIZED_MESSAGE = "The request is missing a valid Authorization token."
    UNSUPPORTED_MEDIA_TYPE_MESSAGE = "Unsupported Media Type"
    CONFLICT_MESSAGE = "Duplicate Entry"

    AUTHORIZATION_TOKEN_EXPIRED = "Authorization token is expired."
    AUTHORIZATION_TOKEN_SIGNATURE_INVALID = "Authorization token signature is invalid."


    def __init__(self) :
        pass

    def handle_error (code , message , status) :
        response = jsonify(
            {   "status_code" : code ,
                "error" : {
                    "code" : code ,
                    "message" : message ,
                    "status" : status
                }
            }
        )
        return response
