#!/usr/bin/yarn dev
import sinon from "sinon";
import { expect } from "chai";
import { createQueue } from "kue";
import createPushNotificationsJobs from "./8-job";

describe("createPushNotificationsJobs", () => {
  const SPY_TEST = sinon.spy(console);
  const QUEUE = createQueue({ name: "push_notification_code_test" });

  before(() => {
    QUEUE.testMode.enter(true);
  });

  after(() => {
    QUEUE.testMode.clear();
    QUEUE.testMode.exit();
  });

  afterEach(() => {
    SPY_TEST.log.resetHistory();
  });

  it("display an error message if jobs is not an array", () => {
    expect(
      createPushNotificationsJobs.bind(createPushNotificationsJobs, {}, QUEUE)
    ).to.throw("Jobs is not an array");
  });

  it("adds jobs to the queue with the correct type", (done) => {
    expect(QUEUE.testMode.jobs.length).to.equal(0);
    const jobInfos = [
      {
        phoneNumber: "105771220",
        message: "Use the code 2023 to verify your account",
      },
      {
        phoneNumber: "105771222",
        message: "Use the code 2024 to verify your account",
      },
    ];
    createPushNotificationsJobs(jobInfos, QUEUE);
    expect(QUEUE.testMode.jobs.length).to.equal(2);
    expect(QUEUE.testMode.jobs[0].data).to.deep.equal(jobInfos[0]);
    expect(QUEUE.testMode.jobs[0].type).to.equal("push_notification_code_3");
    QUEUE.process("push_notification_code_3", () => {
      expect(
        SPY_TEST.log.calledWith(
          "Notification job created:",
          QUEUE.testMode.jobs[0].id
        )
      ).to.be.true;
      done();
    });
  });

  it("registers the progress event handler for a job", (done) => {
    QUEUE.testMode.jobs[0].addListener("progress", () => {
      expect(
        SPY_TEST.log.calledWith(
          "Notification job",
          QUEUE.testMode.jobs[0].id,
          "25% complete"
        )
      ).to.be.true;
      done();
    });
    QUEUE.testMode.jobs[0].emit("progress", 25);
  });

  it("registers the failed event handler for a job", (done) => {
    QUEUE.testMode.jobs[0].addListener("failed", () => {
      expect(
        SPY_TEST.log.calledWith(
          "Notification job",
          QUEUE.testMode.jobs[0].id,
          "failed:",
          "Failed to send"
        )
      ).to.be.true;
      done();
    });
    QUEUE.testMode.jobs[0].emit("failed", new Error("Failed to send"));
  });

  it("registers the complete event handler for a job", (done) => {
    QUEUE.testMode.jobs[0].addListener("complete", () => {
      expect(
        SPY_TEST.log.calledWith(
          "Notification job",
          QUEUE.testMode.jobs[0].id,
          "completed"
        )
      ).to.be.true;
      done();
    });
    QUEUE.testMode.jobs[0].emit("complete");
  });
});
