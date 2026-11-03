# Example outputs

All images and videos here except `graph_screenshot.png` are AI-generated (`frames.png` is frames cut from an AI-generated video). Each generated PNG embeds the full ComfyUI graph
and prompt (drag it onto ComfyUI to reload the exact run). None of them is edited.

## Real look and video (Comfy Cloud, 2026-11-03 ET)

| Output | Input | Workflow | Settings |
|---|---|---|---|
| `outputs/real/hero_b.png` (880x1184) | image 1 `inputs/pull_01_hippo.png` | `workflows/capamari-first-pull-real.json` (as shipped) | Lightning off: 40 steps, CFG 4, euler / simple, seed `424242424242` |
| `outputs/real/hero_a.png` (880x1184) | image 1 `inputs/pull_01_hippo.png` | same workflow | same, seed `677909188488042` |
| `outputs/capamari_sway.mp4` (8.04 s, 704x960, 25 fps, H.264 + AAC) | `outputs/real/hero_b.png` as `capamari_hero_real.png` | `workflows/capamari-video.json` (LTX-2.3 i2v with audio) | seed `20261103`, distilled LoRA 0.5, as in the template |
| `outputs/frames.png` | `outputs/capamari_sway.mp4` | `ffmpeg -i capamari_sway.mp4 -vf "fps=6/8,scale=234:-1,tile=6x1" -frames:v 1 frames.png` | six frames, one every 1.33 s |

The PNGs and the MP4 embed their ComfyUI graph and prompt. A first video attempt (orbit prompt on the C4D capsule)
morphed after ~4 s and was deleted.

## C4D look and roll

Models for all: `qwen_image_edit_2511_fp8mixed`, `qwen_2.5_vl_7b_fp8_scaled`, `qwen_image_vae`, and for Lightning runs
the `Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16` LoRA. Sampler euler / simple, seed `677909188488042`, Comfy Cloud.

| Output | Input | Workflow | Settings | Run date (ET) |
|---|---|---|---|---|
| `outputs/capamari_first_pull_c4d.png` (880x1184) | image 1 `inputs/pull_01_hippo.png` | `workflows/capamari-first-pull.json`, prompt `first_pull` | Lightning off: 40 steps, CFG 4 | 2026-11-03 |
| `outputs/series/pull_02.png` (880x1184) | image 1 `outputs/capamari_first_pull_c4d.png`, image 2 `inputs/pull_02_netsuke.png` | `workflows/capamari.json`, prompt = one inventory sentence + `roll` (see README) | Lightning on: 4 steps, CFG 1 | 2026-11-03 |
| `outputs/capamari_roll_00001_.png` (880x1184) | image 1 `inputs/pull_01_hippo.png` (raw photo, no first-pull capsule), image 2 `inputs/pull_02_netsuke.png` | earlier version of `workflows/capamari.json` (older roll prompt) | Lightning on: 4 steps, CFG 1 | 2026-11-02 |
| `outputs/graph_screenshot.png` | | Screenshot of the earlier roll graph after that 2026-11-02 run; browser tab bar cropped off | | 2026-11-02 |

Later rolls (watch, toy) did not keep the earlier objects and are not included; see Known limitation in the README.
