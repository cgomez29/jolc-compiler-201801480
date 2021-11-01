import React from "react";

const Table = ({ headers, data }) => {
  if (data !== "") {
    // var value = JSON.stringify( JSON.parse( data ))
    data = JSON.parse(data);
  } else {
    data = [
      {
        column1: " -- ",
        column2: " -- ",
        column3: " -- ",
        column4: " -- ",
        column5: " -- ",
      },
    ];
  }

  return (
    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">{headers.head1}</th>
          <th scope="col">{headers.head2}</th>
          <th scope="col">{headers.head3}</th>
          <th scope="col">{headers.head4}</th>
          <th scope="col">{headers.head5}</th>
        </tr>
      </thead>
      <tbody>
        {data.map(({ column1, column2, column3, column4, column5 }, i) => (
          <tr class="table-light" key={i}>
            <th scope="row">{column1}</th>
            <td>{column2}</td>
            <td>{column3}</td>
            <td>{column4}</td>
            <td>{column5}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default Table;
