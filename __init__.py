from comfy_api.latest import ComfyExtension, io
from typing_extensions import override

from .minimax_director import MiniMaxH3Director
from .minimax_chain import MiniMaxH3DirectorChain
from .minimax_enhance import MiniMaxH3EnhancePrompt
from .minimax_lastframe import MiniMaxH3SaveLastFrame
from .minimax_preview import MiniMaxH3PreviewOverride
from .minimax_retake import MiniMaxH3RetakeStitch

# MiniMaxH3DirectorChain is registered again (0.3.4): the Director now exposes a
# timeline_data output, so one wire hands the Chain the timeline — the UX gap that
# had it withdrawn. See minimax_chain.py for the design notes.


class MiniMaxH3DirectorExtension(ComfyExtension):
    @override
    async def get_node_list(self) -> list[type[io.ComfyNode]]:
        return [MiniMaxH3Director, MiniMaxH3DirectorChain, MiniMaxH3PreviewOverride,
                MiniMaxH3RetakeStitch, MiniMaxH3EnhancePrompt,
                MiniMaxH3SaveLastFrame]


async def comfy_entrypoint() -> MiniMaxH3DirectorExtension:
    return MiniMaxH3DirectorExtension()


NODE_CLASS_MAPPINGS = {
    "MiniMaxH3DirectorCS": MiniMaxH3Director,
    "MiniMaxH3DirectorChainCS": MiniMaxH3DirectorChain,
    "MiniMaxH3PreviewOverrideCS": MiniMaxH3PreviewOverride,
    "MiniMaxH3RetakeStitchCS": MiniMaxH3RetakeStitch,
    "MiniMaxH3EnhancePromptCS": MiniMaxH3EnhancePrompt,
    "MiniMaxH3SaveLastFrameCS": MiniMaxH3SaveLastFrame,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MiniMaxH3DirectorCS": "MiniMax H3 Director",
    "MiniMaxH3DirectorChainCS": "MiniMax H3 Director Chain",
    "MiniMaxH3PreviewOverrideCS": "MiniMax H3 Preview Override",
    "MiniMaxH3RetakeStitchCS": "MiniMax H3 Retake Stitch",
    "MiniMaxH3EnhancePromptCS": "MiniMax H3 Enhance Prompt",
    "MiniMaxH3SaveLastFrameCS": "MiniMax H3 Save Last Frame",
}

WEB_DIRECTORY = "./js"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
