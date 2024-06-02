import React from 'react'

const TagsCards = ({ text, colorTag ,textColor }) => {
    return (
      <div className={` ${colorTag} h-6 w-fit rounded-sm  `} >
          <p className={`px-2 ${textColor}  text-base text-center `} >{text}</p>
      </div>
    )
  }

export default TagsCards