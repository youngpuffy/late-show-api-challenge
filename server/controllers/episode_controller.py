from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from server.models import db
from server.models.episode import Episode

episode_bp = Blueprint('episode', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def list_episodes():
    episodes = Episode.query.all()
    return jsonify ([{'id': e.id, 'number': e.number, 'date':e.date} for e in episodes])

@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    return jsonify({
        'id': episode.id,
        'number': episode.number,
        'date':episode.date,
        'appearances':[
            {
                'id': a.id,
                'guest_id': a.guest_id,
                'guest_name': a.guest.name,
                'rating': a.rating
            } for a in episode.appearances
        ]
    })
@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify(message='Episode and appearance deleted'), 200