# UserWarning

Setup `UserWarning` before all the modules you wanna to apply

```

import warnings
warnings.simplefilter("ignore", UserWarning)

import the_module_that_warns
```