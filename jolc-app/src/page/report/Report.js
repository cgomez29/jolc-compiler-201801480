import React, { useContext } from "react";
import Table from "../../components/Table/Table";
import { UserContext } from "../../context/UserContext";

import "./Report.css";

export const Report = () => {
  const { symbols } = useContext(UserContext);

  const headers = {
    head1: "Name",
    head2: "Type",
    head3: "Scope",
    head4: "Row",
    head5: "Column",
  };

  return (
    <div className="container">
      <h1>Reports</h1>
      <div className="row">
        <h3>Symbols table</h3>
        <Table headers={headers} data={symbols} />
      </div>
    </div>
  );
};
