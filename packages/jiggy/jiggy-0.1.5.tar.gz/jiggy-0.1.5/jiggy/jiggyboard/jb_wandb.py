#
# Jiggyboard interface to wandb
#

import wandb

from ..login import window_open
from ..user import authenticated_user, all_teams, Team

from .artifact_source import ArtifactService, ArtifactSource, ArtifactSourceRequest

from .jiggy_session import session

from .board import get_board, create_board


def create_artifact_source(team    : Team = None,
                           api_key : str  = None,
                           host    : str  = "api.wandb.ai") -> ArtifactSource:
    """
    Create a Weights & Biases ArtifactSource

    If team is None then will use user's default team (as specified in User.default_team_id
    api_key is the wandb api key to use to access the artifacts stored on wandb. 
    host is the wandb api hostname, defaulting to api.wandb.ai
    """
    if team is None:
        # get user default team
        # not sure this is a good idea, may want to require team
        team_id = authenticated_user().default_team_id
    else:
        team_id = Team.id

    if not api_key:
        # prompt user for wandb key
        window_open("https://%s/authorize" % host.split('.',1)[1])
        api_key = input("Enter your wandb.ai API Key: ")
    # api key validation will occur server side
    rsp = session.post(f'/teams/{team_id}/artifact_sources', model=ArtifactSourceRequest(host    = host,
                                                                                         api_key = api_key,
                                                                                         source  = ArtifactService.wandb))
    return ArtifactSource(**rsp.json())





def jb_wandb_init():
    """
    wandb specific leaderboard init code
    """
    api = wandb.apis.PublicApi()

    proj = api.project(wandb.run.project)

    board = get_board(wandb.run.project)
    if board:
        print(f"Found existing leaderboard: {board.name}")
    else:
        board = create_board(wandb.run.project)
        print(f"Created leaderboard to match current wandb project: {board.name}")

    watchers = board.artifact_watchers()
    if watchers:
        print("Found existing Artifact Watchers:")
        for w in watchers:
            print(f"{w.jiggy_type:8} {w.name}")
        return

    print(f"Found the following artifact collections in wandb project {proj.name}:")    
    collections = []
    count = 0
    for atype in proj.artifacts_types():
        for c in atype.collections():
            cname = f"{c.entity}/{c.project}/{c.name}"
            collections.append(cname)
            print(f" {count:2}: {atype.name+':':12}   {cname}")
            count += 1
            
    print()
    if len(collections) < 2:
        print("Upload model and dataset artifacts in wanbd project and re-run jiggy.init()")
        return

    def query_collection(jiggy_type):
        artifact = ""
        while artifact not in collections:
            artifact = input(f"{jiggy_type} artifact collection name to evaluate in this leaderboard: ")
            artifact = artifact.rstrip()
            try:
                artifact = collections[int(artifact)]
            except:
                pass
        return artifact
    
    data_artifact = query_collection('dataset')    
    model_artifact = query_collection('model')

    print("Creating wandb artifact source and artifact watchers:")
    wandb_store = create_artifact_source(api_key=api.api_key)

    board.create_artifact_watcher(wandb_store, 'model',   model_artifact)
    board.create_artifact_watcher(wandb_store, 'dataset', data_artifact)

    for w in board.artifact_watchers():
        print(f"{w.jiggy_type:6} w.name")
    print(f"\nCreate an evaluation code artifact in {wandb.run.project} and associated leaderboard watcher to complete leaderboard configuration.")


