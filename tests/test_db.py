from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(username='teste', password='senha', email='teste@mail.com')
    session.add(user)
    session.commit()
    result = session.scalar(select(User).where(User.email == 'teste@mail.com'))

    assert result.email == 'teste@mail.com'
