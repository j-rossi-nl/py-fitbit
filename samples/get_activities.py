import json

from fitbit import ApiClient
from fitbit import Configuration
from fitbit.api import ActivityApi


def main():
    with open("auth_data.txt") as src:
        auth_data = json.load(src)

    config = Configuration()
    config.access_token = auth_data["access_token"]

    api_client = ApiClient(configuration=config)
    api_client.set_default_header(
        header_name="X-Fitbit-Subscriber-Id", header_value=auth_data["user_id"]
    )

    activity = ActivityApi(api_client=api_client)
    activity.get_activities_log_list(
        after_date="2022-01-01", sort="asc", offset=0, limit=20
    )

    data = json.loads(api_client.last_response.data)
    print(data)


if __name__ == "__main__":
    main()
    exit()
