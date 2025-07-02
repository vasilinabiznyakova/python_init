

# example 1
def fetch_from_mono():
    pass

def fetch_from_pumb():
    pass


def fetch_data(provider="mono"):
    if provider == "mono":
        return fetch_from_mono
    elif provider == "pumb":
        return fetch_from_pumb
    else:
        raise ValueError("Unknown Provider")


fetch = fetch_data("mono")
print(fetch)

# example 2
# def fetch_data_from_monobank(id, success, failure): #callback
#     try:
#         requests.get(id)
#         success()
#     except Exception as  e:
#         failure(e)

# def save_data_on_disk():
#     print("Saving on disk")

# def handle_error(e):
#     print(e)


# fetch_data_from_monobank("1234", save_data_on_disk, handle_error)
