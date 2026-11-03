# Sources

All input images are public-domain (CC0 1.0) objects released by The Metropolitan Museum of Art under its
Open Access policy. Each object was checked on 2026-11-02 (ET) with the Met Collection API
(`/public/collection/v1/objects/<id>` returned `isPublicDomain: true`). Originals were downloaded from the
`primaryImage` URL, converted to RGB, downscaled with Lanczos to a longest side of at most 1536 px and saved as PNG
(no metadata kept). No people photographed, no logos, no client material.

CC0 terms: https://creativecommons.org/publicdomain/zero/1.0/ ; Met Open Access policy:
https://www.metmuseum.org/policies/image-resources

| File | Object | Met object page | Original image | Original SHA-1 | License |
|---|---|---|---|---|---|
| `inputs/pull_01_hippo.png` (1151x1536, from 2899x3870 JPEG) | Hippopotamus ("William"), ca. 1961–1878 B.C.. Egypt, Middle Kingdom. Acc. no. 17.9.1 | https://www.metmuseum.org/art/collection/search/544227 | https://images.metmuseum.org/CRDImages/eg/original/DP248993.jpg | `a53d057d6842838f61be07139232e5c4adb25b8c` | CC0 1.0 (Met Open Access, `isPublicDomain: true` via the Met Collection API) |
| `inputs/pull_02_netsuke.png` (1536x1024, from 4000x2667 JPEG) | Netsuke, 18th century. Japan. Acc. no. 10.211.2273 | https://www.metmuseum.org/art/collection/search/59356 | https://images.metmuseum.org/CRDImages/as/original/LC-10_211_2273_001.jpg | `a5ea2f69ab42f61c4dad1c50d9eee08049cdb67a` | CC0 1.0 (Met Open Access, `isPublicDomain: true` via the Met Collection API) |
| `inputs/pull_03_watch.png` (1428x1536, from 3530x3797 JPEG) | Watch, ca. 1630–40. Johann Possdorfer. Acc. no. 17.190.1525 | https://www.metmuseum.org/art/collection/search/194118 | https://images.metmuseum.org/CRDImages/es/original/DP169988.jpg | `3bdc3a1571b2fec61bfcc24ec94513d155df123f` | CC0 1.0 (Met Open Access, `isPublicDomain: true` via the Met Collection API) |
| `inputs/pull_04_toy.png` (1344x1536, from 1736x1984 JPEG) | Toy, 19th century. China. Acc. no. 67.179.18a, b | https://www.metmuseum.org/art/collection/search/51363 | https://images.metmuseum.org/CRDImages/as/original/DP14311.jpg | `9d3ed27f1a31b0b6f7ab12d0e483e602084b12d7` | CC0 1.0 (Met Open Access, `isPublicDomain: true` via the Met Collection API) |

Generated outputs are listed in `examples/README.md` with the input, workflow, seed and model files used for each one.
