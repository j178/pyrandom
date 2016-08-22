#pyrandom
Convenient Python lib for [random.org](https://random.org)

## Requirements
- requests

## Usage
1. You need to get a api key from [random.org](https://api.random.org/api-keys/beta)
2. Clone this repository or install this package through `pip install pyrandom`
3. Import this module and code
  ```python
  import pyrandom
  # Recommend to store your key in a config file and import here
  pyrandom.set_api_key('your-key') 

  nums = pyrandom.generate_integers(n=10, min=1, max=1000)
  ```
