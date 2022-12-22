from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'blogwizardstorage'
    account_key = '5wFzyjAFqdlVhIfHZLNjeLTknydtBIXHsFRWxyxCtc7IECENtgqfWBS4N+XWnlFGytS3DnLgeq4M+ASth/rWGQ==' 
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'blogwizardstorage'
    account_key = '5wFzyjAFqdlVhIfHZLNjeLTknydtBIXHsFRWxyxCtc7IECENtgqfWBS4N+XWnlFGytS3DnLgeq4M+ASth/rWGQ=='
    azure_container = 'static'
    expiration_secs = None