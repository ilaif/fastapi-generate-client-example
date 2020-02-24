import my_server_client


def main():
    client_configuration = my_server_client.Configuration(
        host='http://localhost:8000',
    )
    client = my_server_client.ApiClient(
        configuration=client_configuration,
    )
    api = my_server_client.DefaultApi(
        api_client=client,
    )

    api.create_user_users_post(
        user={
            'name': 'pycon',
        },
    )

    print(api.get_users_users_get())


if __name__ == '__main__':
    main()
