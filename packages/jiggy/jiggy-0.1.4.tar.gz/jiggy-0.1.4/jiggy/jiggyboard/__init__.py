# Jiggyboard Client

from .artifact_source import artifact_sources

from .board import create_board, boards, get_board, results


import jiggy.jiggyboard.jb_wandb as wandb    
    

def init():
    wandb.jb_wandb_init()
    
