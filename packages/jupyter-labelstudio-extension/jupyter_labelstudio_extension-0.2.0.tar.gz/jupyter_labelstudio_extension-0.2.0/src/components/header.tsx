import React from "react";

// @ts-ignore
import Link from './link';

const Header = () => {
  // @ts-ignore
  return (
    <div className="ui secondary pointing menu">
      <Link href="/" className="item">
        Create Project
      </Link>
      <Link href="/label" className="item">
        Label Project
      </Link>
    </div>
  );
};

export default Header;
