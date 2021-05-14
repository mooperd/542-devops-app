"""Logged-in page routes."""
from flask import Blueprint, flash, redirect, render_template, url_for, request
from flask_login import current_user, login_user

# Blueprint Configuration
root_bp = Blueprint(
    'root_bp', __name__
)


@root_bp.route("/")
def root():
    """Root route"""
    if current_user.is_authenticated:
        return redirect(url_for('pages_bp.races'))
    else:
        return redirect(url_for('auth_bp.login'))


@root_bp.route("/healthz")
def healthz():
    """Health check"""
    return "OK"

