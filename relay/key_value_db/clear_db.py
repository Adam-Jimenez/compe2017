# serialize DB

import pickle
with open('database', 'wb') as f:
    pickle.dump({}, f)
