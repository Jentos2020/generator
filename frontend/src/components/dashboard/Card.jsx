import React from 'react';

const Card = ({ props }) => {
    return (
        <div className="col-xl-3 col-sm-6 col-12 mt-3">
            <div className={`rounded shadow p-3 border-bottom border-${props.color} border-4`}>
                <div className="card-body">
                    <div className="row">
                        <div className="col">
                            <span className="h6 font-semibold text-muted text-sm d-block mb-2">
                                {props.name}
                            </span>
                            <span className="h3 font-bold mb-0 ">
                                {props.body}
                            </span>
                        </div>
                        <div className="col-auto">
                            <div className="text-success">
                                <h3><i className={props.icon}></i></h3>
                            </div>
                        </div>
                    </div> 

                    {props.badge === true
                        ? <div className="mt-2 mb-0 text-sm">
                            {props.badgeBody > 0
                                ? <span className="badge text-bg-success me-2">
                                    <i className="bi bi-arrow-up me-1"></i>
                                    +{props.badgeBody}%
                                </span>
                                : <span className="badge text-bg-danger me-2">
                                    <i className="bi bi-arrow-down me-1"></i>
                                    {props.badgeBody}%
                                </span>
                            }
                            <span className="text-secondary-emphasis">
                                {props.badgeText}
                            </span>
                        </div>
                        : <div className="mt-2 mb-0 text-sm">
                            <span className="text-secondary-emphasis">
                                {props.badgeText}
                            </span>
                        </div>
                    }
                </div>
            </div>
        </div>
    );
};

export default Card;