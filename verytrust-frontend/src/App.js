import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, useNavigate, useParams } from 'react-router-dom';
import axios from 'axios';
import './App.css';
import { FaUserFriends, FaLock, FaCalendarAlt, FaUserPlus, FaTwitter, FaSearchLocation, FaUser } from 'react-icons/fa';
import { FiSettings, FiRefreshCcw, FiSearch } from 'react-icons/fi';
import { MdOutlineNotificationsNone } from 'react-icons/md';
import { BsThreeDotsVertical } from 'react-icons/bs';
import { IoArrowBack } from 'react-icons/io5';

function Home() {
  const [username, setUsername] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (username) {
      navigate(`/user/${username}`);
    }
  };

  return (
    <div className="phone-frame">
      <div className="user-details-container">
        <div className="user-details-header">
          <MdOutlineNotificationsNone className="icon" />
          <h1>Scan</h1>
          <BsThreeDotsVertical className="icon" />
        </div>
        <div className="home user-details-info">
          <h1 style={{"text-align":"center"}}>Obtenir le score de l'utilisateur</h1>
          <form onSubmit={handleSubmit}>
            <input
              className='input-home'
              type="text"
              placeholder="Entrer le nom d'utilisateur"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
            <button  className='button-home' type="submit">Obtenir le score</button>
          </form>
        </div>
      </div>
    </div>
  );
}

function UserDetails({ username }) {
  const [userData, setUserData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  React.useEffect(() => {
    const controller = new AbortController();
    const fetchUserData = async () => {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/user_score', {
          username: username,
        }, { signal: controller.signal });
        setUserData(response.data);
        setLoading(false);
      } catch (err) {
        if (axios.isCancel(err)) {
          console.log('Request canceled', err.message);
        } else {
          setError('Erreur lors de la récupération des données utilisateur');
          setLoading(false);
        }
      }
    };

    fetchUserData();
    return () => {
      controller.abort();
    };
  }, [username]);

  if (loading) return <div>Chargement...</div>;
  if (error) return <div>{error}</div>;

  return (
    <div className="phone-frame">
      <div className="user-details-container">
        <div className="user-details-header">
          <IoArrowBack className="icon" onClick={() => navigate('/')} />
          <h1>Scan</h1>
          <BsThreeDotsVertical className="icon" />
        </div>
        <div className="user-details-info">
          <div className="user-details-avatar">
            <div className="avatar-circle">
              <FaUser color='white' className="icon avatar-icon"/>
            </div>
            <h2>{userData.username}</h2>
          </div>
          <div className="user-details-score">
            <div className="score-circle">
              <span>{userData.score}</span>
            </div>
          </div>
        </div>
        <div className="user-details-icons-grid">
          <div className="icon-block">
            <FaCalendarAlt className="icon" />
            <p>{new Date(userData.created_at).toLocaleDateString('fr-FR')}</p>
          </div>
          <div className="icon-block">
            <FaUserFriends className="icon" />
            <p>{userData.followers_count.toLocaleString('fr-FR')} Abonnés</p>
          </div>
          <div className="icon-block">
            <FaUserPlus className="icon" />
            <p>{userData.following_count} Abonnements</p>
          </div>
          <div className="icon-block">
            <FaTwitter className="icon" />
            <p>{userData.tweet_count} Tweets</p>
          </div>
          <div className="icon-block">
            <FaLock className="icon" />
            <p>{userData.protected ? 'Privé' : 'Public'}</p>
          </div>
          <div className="icon-block">
            <FaSearchLocation className="icon" />
            <p>{userData.location}</p>
          </div>
        </div>
        <div className="user-details-footer">
          <div className="footer-icon">
            <FiSearch />
            <p>News</p>
          </div>
          <div className="footer-icon">
            <FiRefreshCcw />
            <p>Scan</p>
          </div>
          <div className="footer-icon">
            <FiSettings />
            <p>Setting</p>
          </div>
        </div>
      </div>
    </div>
  );
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route
          path="/user/:username"
          element={<UserDetailsWrapper />}
        />
      </Routes>
    </Router>
  );
}

function UserDetailsWrapper() {
  const { username } = useParams();
  return <UserDetails username={username} />;
}

export default App;
