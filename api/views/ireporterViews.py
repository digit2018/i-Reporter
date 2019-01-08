from flask import Blueprint
from api.controllers.ireportercontrollers import addUser, add_red_flag, add_intervention, getAllIncidents, searchId, incidents, deleteId, edit_incident


bp = Blueprint("ireporterViews", __name__, url_prefix="/api/v1")

@bp.route("/users", methods=["POST"])
def createUser():
    return addUser()

@bp.route("/red-flags", methods=["POST"])

def createIncident():
    return addIncident()

@bp.route("/red-flags", methods=["GET"])
def get_all_red_flag_records():
    return getAllIncidents()

@bp.route("/red-flags/<int:red_flag_id>", methods=["GET"])

def get_specific_redflag(red_flag_id):
    return searchId(red_flag_id, incidents)

@bp.route("/red-flags/<int:red_flag_id>/location", methods=["PATCH"])
def edit_specific_redflag_location():
    pass

@bp.route("/red-flags/<int:red_flag_id>/comment", methods=["PATCH"])
def add_comment_to_specific_redflag_record():
    pass


@bp.route("/incidents/<int:incid_id>", methods=["DELETE"])
def delete_specific_redflag_record(incid_id):
    return deleteId(incid_id, incidents)



