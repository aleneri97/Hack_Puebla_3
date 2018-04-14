import React, { Component } from 'react';

class Mood extends Component{
    constructor(props){
        super(props);
        this.state={
            isActive: false
        }

        this.handleClick = this.handleClick.bind(this);
    }

    handleClick(){
        this.setState(prev=>({
            isActive: !prev.isActive
        }));
    }

    render(){
        return(
            <div className={this.state.isActive ? 'mood mood-active': 'mood'}>
                <img src={this.props.url} alt="" className="img-responsive" onClick={this.handleClick}/>
            </div>
        )
    }
}

export default class MoodBox extends Component{
    constructor(props){
        super(props);
        this.state = {
            active: 1
        }
        this.handleMoodClick = this.handleMoodClick.bind(this);
    }

    handleMoodClick(e){
        this.setState({
            active: e.key
        })
    }
    
    componentDidMount(){
        console.log(this.state.active);
    }

    render() {
        const emojisPath = ['images/happy.jpg', 'images/happy.jpg', 'images/happy.jpg', 'images/happy.jpg'];
        const moods = emojisPath.map((mood, counter) =>
            <Mood url={mood} key={counter}  onClick={this.handleMoodClick}/>
        );
        return (
            <div className="box">
                <p className="text">¿Cómo te sientes?</p>
                <div className="mood-box" onClick={this.handleMoodClick}>
                    {moods}
                </div>
            </div>
        );
    }
}