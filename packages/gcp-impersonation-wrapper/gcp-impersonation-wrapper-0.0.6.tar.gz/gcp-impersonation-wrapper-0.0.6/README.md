# GCP Impersonation wrapper

The gcp-impersonation-wrapper is a small util used to impersonate service accounts using service account. We pass the main credentials, list service accounts we can impersonate and then actually impersonate like so:

```py
#!/usr/bin/env python3
from src.service_account import ServiceAccount


if __name__ == "__main__":
    # Insert credentials here
    credentials = None

    service_account = ServiceAccount(
        project_id="your-project-id",
        impersonator_credentials=credentials
    )

    # Can be used in a with statement
    with service_account.impersonate(
        service_account_email="your-service-account-email",
        target_scopes=["https://www.googleapis.com/auth/cloud-platform"],
        service="iam",
        version="v1"
    ) as impersonated_service_account:
        # do something with the impersonated service account
        service_accounts_the_impersonated_sacc_can_see = impersonated_service_account.service.projects(
        ).serviceAccounts().list().execute()
        print(service_accounts_the_impersonated_sacc_can_see)

    # Or as a variable
    impersonated_service_account = service_account.impersonate(
        service_account_email="your-service-account-email",
        target_scopes=["https://www.googleapis.com/auth/cloud-platform"],
        service="iam",
        version="v1"
    )
    service_accounts_the_impersonated_sacc_can_see = impersonated_service_account.service.projects(
    ).serviceAccounts().list().execute()
```

To list the impersonatable service accounts we do:
```py
#!/usr/bin/env python3
from src.service_account import ServiceAccount


if __name__ == "__main__":
    # Insert credentials here
    credentials = None

    service_account = ServiceAccount(
        project_id="your-project-id",
        impersonator_credentials=credentials
    )

    # This returns a list of email like ["john@doe.com", "jane@doe.com", ....]
    service_account_emails_we_can_impersonate = service_account.list_all_impersonatable_service_account_emails() 
```