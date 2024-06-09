import React from 'react';
import TagsCards from './tagsCards';
import cardImage from '../../assets/img/card-image.png';
import flagIcon from '../../assets/img/Flag.svg';
import userImg from '../../assets/img/userimg.png';
import commentsIcon from '../../assets/svg/commentsIcon.svg'
import filesIcon from '../../assets/svg/filesIcon.svg'
import moreHorizontal from '../../assets/svg/more-horizontal.svg'

const cardInfo = {
    tags: ['Bugs', 'Feedback', 'Algo'],
    title: "Improve cards titulo",
    img: cardImage,
    date: '21/03/22',
    timeLeft: 18,
    comments: 16,
    files: 0,
};

const Card = () => {
  return (
    <article className='m-4 w-72'>
        {/* Tags */}
        <div className="flex space-x-2">
            {cardInfo.tags.map((tag, index) => (
                <TagsCards key={index} text={tag} colorTag="bg-greentag" textColor="text-greentexttag" />
            ))}
        </div>
        {/* Title & button actions */}
        <div className="flex justify-between items-center mt-2">
            <h3 className="text-lg ">{cardInfo.title}</h3>
            <button className='h-5 w-5 border border-slate-400 rounded-md text-center flex items-center justify-center'><img src={moreHorizontal} alt="" /></button>
        </div>
        {/* Image */}
        {cardInfo.img && (
            <div className="mt-2"> 
                <img src={cardInfo.img} alt="Card Image" />
            </div>
        )}
        {/* Deadline & time left */}
        <div className="flex justify-between items-center mt-2">
            <div className="flex items-center justify-center space-x-1">
                <img src={flagIcon} alt="Flag Icon"  />
                <p>{cardInfo.date}</p>
            </div>
            <h6>D-{cardInfo.timeLeft}</h6>
        </div>
        {/* Ticket Information */}
        <div className="flex items-center justify-between mt-2">
            <img src={userImg} alt="User" className="w-6 h-6 rounded-full" />
            <div className="flex items-center space-x-2 ml-2">
                <div className="flex items-center space-x-1">
                    <img src={commentsIcon} alt="Comments Icon" /> 
                    <p>{cardInfo.comments} comments</p>
                </div>
                <div className="flex items-center space-x-1">
                    <img src={filesIcon} alt="Files Icon" /> 
                    <p>{cardInfo.files} files</p>
                </div>
            </div>
        </div>
    </article>
  );
}

export default Card;