class RolesCache:
    def __init__(self, capacity):
        # Add any additional state you may need.
        self.capacity

    def get(self, role):
        # Returns the message corresponding to the last invocation of that role, None if the role does not exist in the cache.
        print("Your role is")

    def set(self, role, message):
        # Adds the role and its corresponding message to the cache.
        # If the role already exists, only the message is updated. Otherwise, the oldest role is removed to make space.
        add_role(self.roles)

    def _complexity(self):
        return {
            'get': 'O(1)',
            'set': 'O(2)',
            'space': 'O(3)'
        }