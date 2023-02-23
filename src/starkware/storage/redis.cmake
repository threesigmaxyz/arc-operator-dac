python_lib(starkware_storage_redis_lib
    PREFIX starkware/storage

    FILES
    redis_storage.py

    LIBS
    starkware_storage_lib
    pip_redis
)
