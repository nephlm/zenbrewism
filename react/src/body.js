
import React from 'react';
import axios from 'axios';
import ReactMarkdown from 'react-markdown'
import './index.css';

export class Content extends React.Component {
  render() {
    return (
      <div className="outer-left">
        <div className="content">
          <img className="book-title center" src="StolenSong_Title.png" />
          <p className="book-subtitle">
            Sylph's Symphony Number 1
          </p>
          <Blurb/>
        </div>
      </div>
    );
  }
}

export class Blurb extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      content: ""
    };
  }

  componentDidMount() {
    axios.get('/api/home')
      .then(function(response) {
        console.log(response.data.text);
        this.setState({
            isLoaded: true,
            content: response.data.text
          });
      }.bind(this))
      .catch(function(error) {
        console.log(error)
      });
  }

  render() {
    return (
        <div>
          <ReactMarkdown source={this.state.content} />
        </div>
    );
  }
}
