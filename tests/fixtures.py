"""
decoded AUTH_HEADER (newlines added for readability):
{
    "identity": {
        "account_number": "1234",
        "internal": {
            "org_id": "5678"
        },
        "type": "User",
        "user": {
            "email": "test@example.com",
            "first_name": "Firstname",
            "is_active": true,
            "is_internal": true,
            "is_org_admin": false,
            "last_name": "Lastname",
            "locale": "en_US",
            "username": "test_username"
        }
    }
    "entitlements": {
        "smart_management": {
            "is_entitled": true
        }
    }
}
"""

AUTH_HEADER = {
    "X-RH-IDENTITY": "eyJpZGVudGl0eSI6eyJhY2NvdW50X251bWJlciI6"
    "IjEyMzQiLCJpbnRlcm5hbCI6eyJvcmdfaWQiOiI1"
    "Njc4In0sInR5cGUiOiJVc2VyIiwidXNlciI6eyJl"
    "bWFpbCI6InRlc3RAZXhhbXBsZS5jb20iLCJmaXJz"
    "dF9uYW1lIjoiRmlyc3RuYW1lIiwiaXNfYWN0aXZl"
    "Ijp0cnVlLCJpc19pbnRlcm5hbCI6dHJ1ZSwiaXNf"
    "b3JnX2FkbWluIjpmYWxzZSwibGFzdF9uYW1lIjoi"
    "TGFzdG5hbWUiLCJsb2NhbGUiOiJlbl9VUyIsInVz"
    "ZXJuYW1lIjoidGVzdF91c2VybmFtZSJ9fSwiZW50"
    "aXRsZW1lbnRzIjogeyJzbWFydF9tYW5hZ2VtZW50"
    "IjogeyJpc19lbnRpdGxlZCI6IHRydWUgfX19Cg=="
}


HISTORICAL_PROFILE = {
    "inventory_id": "cd54d888-4ccb-11ea-8627-98fa9b07d419",
    "profile": {
        "salutation": "hi",
        "display_name": "test-system",
        "system_profile_exists": True,
        "installed_packages": [
            "openssl-1.1.1c-2.fc30.x86_64",
            "python2-libs-2.7.16-2.fc30.x86_64",
        ],
        "id": "bbbbbbbb-28ae-11e9-afd9-c85b761454fa",
    },
}

FETCH_SYSTEMS_WITH_PROFILES_RESULT = (
    {
        "account": "9876543",
        "bios_uuid": "e380fd4a-28ae-11e9-974c-c85b761454fb",
        "created": "2018-01-31T13:00:00.100010Z",
        "display_name": "tartuffe",
        "fqdn": "hostname_one",
        "id": "cd54d888-4ccb-11ea-8627-98fa9b07d419",
        "insights_id": "00000000-28af-11e9-9ab0-c85b761454fa",
        "ip_addresses": ["10.0.0.3", "2620:52:0:2598:5054:ff:fecd:ae15"],
        "mac_addresses": ["52:54:00:cd:ae:00", "00:00:00:00:00:00"],
        "rhel_machine_id": None,
        "satellite_id": None,
        "subscription_manager_id": "RHN Classic and Red Hat Subscription Management",
        "system_profile": {
            "salutation": "hi",
            "fqdn": "hostname_one",
            "system_profile_exists": False,
            "id": "bbbbbbbb-28ae-11e9-afd9-c85b761454fa",
            "network_interfaces": [
                {
                    "name": "eth99",
                    "mtu": 3,
                    "ipv4_addresses": ["8.7.6.5"],
                    "ipv6_addresses": ["00:00:01"],
                },
                {"no_name": "foo"},
            ],
        },
        "tags": [],
        "updated": "2018-01-31T14:00:00.500000Z",
    },
)
