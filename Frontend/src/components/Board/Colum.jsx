import React from 'react';

const Colum = ({ title, children }) => {
  return (
    <div className="m-4 p-4 rounded-lg w-72 bg-gray-200">
      <h2 className="text-lg">{title}</h2>
      {children}
    </div>
  );
}

export default Colum;
