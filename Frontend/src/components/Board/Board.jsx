// Board.js
import Colum from "./Colum";
import Card from "../Card/card";

const Board = () => {
  return (
    <div className="flex justify-center">
      <Colum title="To Do">
        <Card
          title="Task 1"
          date="21/03/22"
          timeLeft={18}
          comments={16}
          files={0}
        />
        <Card
          title="Task 2"
          date="22/03/22"
          timeLeft={15}
          comments={12}
          files={2}
        />
      </Colum>
      <Colum title="In Progress">
        <Card
          title="Task 3"
          date="23/03/22"
          timeLeft={12}
          comments={8}
          files={1}
        />
        <Card
          title="Task 4"
          date="24/03/22"
          timeLeft={10}
          comments={5}
          files={3}
        />
      </Colum>
      <Colum title="Done">
        <Card
          title="Task 5"
          date="25/03/22"
          timeLeft={5}
          comments={3}
          files={0}
        />
        <Card
          title="Task 6"
          date="26/03/22"
          timeLeft={3}
          comments={2}
          files={1}
        />
      </Colum>
    </div>
  );
};

export default Board;
