"""
RestUser is a convenience class for testing RESTful JSON endpoints.
It extends FastHttpUser by adding the `rest`-method, a wrapper around self.client.request() that:
* automatically passes catch_response=True
* automatically sets content-type and accept headers to application/json (unless you have provided your own headers)
* automatically checks that the response is valid json, parses it into a RestResponse and saves it in a field called `js` in the response object.
    (RestResponse support safe navigation so if your json was {"foo": 42}, resp.js["bar"]["baz"] returns None instead of throwing an exception)
* catches any exceptions thrown in your with-block and fails the sample (this probably should have been the default behaviour in Locust)
"""

from contextlib import contextmanager
from locust import task, run_single_user
from locust.contrib.fasthttp import ResponseContextManager
from locust.user.wait_time import constant
from locust_plugins.users import RestUser

# import sys


class MyUser(RestUser):
    host = "https://postman-echo.com"
    wait_time = constant(180)  # be nice to postman-echo.com, and dont run this at scale.

    @task
    def t(self):
        # should work
        with self.rest("GET", "/get", json={"foo": 1}) as resp:
            if resp.js["args"]["foo"] != 1:
                resp.failure(f"Unexpected value of foo in response {resp.text}")

        # should work
        with self.rest("POST", "/post", json={"foo": 1}) as resp:
            if resp.js["data"]["foo"] != 1:
                resp.failure(f"Unexpected value of foo in response {resp.text}")
            # assertions are a nice short way of expressiont your expectations about the response. The AssertionError thrown will be caught
            # and fail the request, including the message and the payload in the failure content
            assert resp.js["data"]["foo"] == 1, "Unexpected value of foo in response"
            # to guard against complete failures (which may make resp.js None), only do the check when error is not already set:
            assert resp.error or resp.js["data"]["foo"] == 1

        # RestResponse support safe navigation returning None if fields are missing (instead of throwing KeyError or
        with self.rest("POST", "/post", json={"foo": 1}) as resp:
            if resp.js["field that doesnt exist"]["status"] != "success":
                resp.failure(f"Bad or missing status in {resp.text}")

        # assertions are a nice short way to validate the response. The AssertionError they raise
        # will be caught by rest() and mark the request as failed

        with self.rest("POST", "/post", json={"foo": 1}) as resp:
            # mark the request as failed with the message "Assertion failed"
            assert resp.js["foo"] == 2

        with self.rest("POST", "/post", json={"foo": 1}) as resp:
            # custom failure message
            assert resp.js["foo"] == 2, "my custom error message"

        with self.rest("POST", "/post", json={"foo": 1}) as resp:
            # use a trailing comma to append the response text to the custom message
            assert resp.js["foo"] == 2, "my custom error message with response text,"

        # this only works in python 3.8 and up, so it is commented out:
        # if sys.version_info >= (3, 8):
        #     with self.rest("", "/post", json={"foo": 1}) as resp:
        #         # assign and assert in one line
        #         assert (foo := resp.js["foo"])
        #         print(f"the number {foo} is awesome")

        # rest() catches most exceptions, so any programming mistakes you make automatically marks the request as a failure
        # and stores the callstack in the failure message
        with self.rest("POST", "/post", json={"foo": 1}) as resp:
            1 / 0  # pylint: disable=pointless-statement

        # response isnt even json, but RestUser will already have been marked it as a failure, so we dont have to do it again
        with self.rest("GET", "/") as resp:
            pass

        with self.rest("GET", "/") as resp:
            # If resp.js is None (which it will be when there is a connection failure, a non-json responses etc),
            # reading from resp.js will raise a TypeError (instead of an AssertionError), so lets avoid that:
            if resp.js:
                assert resp.js["foo"] == 2
            # or, as a mildly confusing oneliner:
            assert not resp.js or resp.js["foo"] == 2

        # 404
        with self.rest("GET", "http://example.com/") as resp:
            pass

        # connection closed
        with self.rest("POST", "http://example.com:42/", json={"foo": 1}) as resp:
            pass


# An example of how you might write a common base class for an API that always requires
# certain headers, or where you always want to check the response in a certain way
class RestUserThatLooksAtErrors(RestUser):
    abstract = True

    @contextmanager
    def rest(self, method, url, **kwargs) -> ResponseContextManager:
        extra_headers = {"my_header": "my_value"}
        with super().rest(method, url, headers=extra_headers, **kwargs) as resp:
            resp: ResponseContextManager
            if resp.js and "error" in resp.js and resp.js["error"] is not None:
                resp.failure(resp.js["error"])
            yield resp


class MyOtherRestUser(RestUserThatLooksAtErrors):
    host = "https://postman-echo.com"
    wait_time = constant(180)  # be nice to postman-echo.com, and dont run this at scale.

    @task
    def t(self):
        with self.rest("GET", "/") as _resp:
            pass


if __name__ == "__main__":
    run_single_user(MyUser)
