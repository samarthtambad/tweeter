import React, {useCallback, useEffect, useState} from 'react'
import logo from './logo.svg';
import './App.css';

function loadTweets(callback) {
  const xhr = new XMLHttpRequest()
  const method = 'GET'
  const url = "http://localhost:8000/api/tweets/"
  const responseType = "json"
  xhr.responseType = responseType
  xhr.open(method, url)
  xhr.onload = function(){
    callback(xhr.response, xhr.status)
  }
  xhr.onerror = function(e) {
    console.log(e)
    callback({"message": "The request was an error"}, 400)
  }
  xhr.send()
  
}

function LikeBtn(props) {
  const {tweet} = props
  return "<button class='btn btn-primary btn-sm' onclick=handleTweetActionBtn(" + 
  tweet.id + "," + tweet.likes + ",'like')>" + tweet.likes + " Likes</button>"
}

function Tweet(props) {
  const {tweet} = props
  const className = props.className ? props.className : 'col-10 mx-auto col-md-6'
  return <div className={className}>
    <p>{tweet.id} - {tweet.content}</p>
    <div className='btn btn-group'></div>
  </div>
}

function App() {
  const [tweets, setTweets] = useState([])

  

  useEffect(() => {
    // do my lookup
    const myCallback = (response, status) => {
      if(status === 200) {
        setTweets(response)
      }
    }
    loadTweets(myCallback)
  }, [])

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <div>
          {tweets.map((item, index) => {
            return <Tweet tweet={item} className="my-5 py-5 border bg-white text-dark" key={`${index}-{item.id}`}/>
          })}
        </div>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
