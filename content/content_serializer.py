class ContentSerializer:
    valid_inputs = {
        "title" : str,
        "module": str,
        "students" : int,
        "description": str,
        "is_active": bool,
    }

    def __init__ (self, **kargs):
        self.data = kargs
        self.errors = {}
    
    def is_valid(self):
        self.clean_data()

        try:
            self.key_validator()
            self.value_validator()
            return True

        except KeyError:
            return False


    def clean_data(self):
        data_keys = set(self.data.keys())

        for key in data_keys:
            if key not in self.valid_inputs.keys():
                self.data.pop(key)
    
    def key_validator(self):
        for key in self.valid_inputs.keys():
            if key not in self.data.keys():
                self.errors[key] = "missing key"
        if self.errors:
            raise KeyError

    def value_validator(self):
        for key, original_type in self.valid_inputs.items():
            if type(self.data[key]) is not original_type:
                self.errors[key] = f"must be a {original_type.__name__}"
        if self.errors:
            raise KeyError
