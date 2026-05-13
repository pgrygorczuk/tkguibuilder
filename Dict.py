from functools import reduce
import utils

class Dict(dict):
	"""An auxiliary class that extends the dictionary's capabilities."""

	@classmethod
	def from_json(cls, path: str) -> "Dict":
		"""Creates a dictionary from a JSON file."""
		return cls(utils.load_json(path))

	def save(self, path: str) -> None:
		"""Saves data to a JSON file."""
		utils.save_json(self, path)

	def get_by_path(self, path: str = "", default = None):
		"""It can read a nested value from the dict based on a given path.
		The path should be composed of words separated by dots
		(e.g: key1.key2.key3)."""
		retval = None
		try:
			retval = reduce(dict.get, path.split("."), self)
		except TypeError as e:
			...
		if retval is None:
			if default is not None:
				return default
			raise KeyError(f"'{path}' does not exist.")
		return retval
	
	def set_by_path(self, path:str, value) -> None:
		"""Puts a value in the given path."""
		keys = path.split(".")
		# Build a dictionary with the appropriate hierarchy.
		def create_entry(i, value):
			if i == len(keys)-1:
				return { keys[i]: value }
			else:
				return { keys[i]: create_entry(i+1, value) }
		# Update recursively.
		def update(d:dict, u:dict):
			for k, v in u.items():
				# if isinstance(v, collections.abc.Mapping):
				if type(v) == dict:
					d[k] = update(d.get(k, {}), v)
				else:
					d[k] = v
			return d
		# Update settings.
		entry = create_entry(0, value)
		update(self, entry)


if __name__ == "__main__":
	d = Dict(a=1, b=2)
	print(d)
	d = Dict.from_json("./settings.json")
	print(type(d), d)
	print("workspace =", d.get_by_path("workspace"))
	d.set_by_path("test1.test2", "test value")
	print(d)
	print(d.get_by_path("non.existing.path"))
