# Li's Local Project

The goal of this repository is to be a local playground, where you can get familiar with dev tools like docker compose,
while building out architectures and implementations for data engineering. The benefits of working locally before moving
to the cloud are:
1. You can iterate quickly and have more access to feedback
2. You can build out complex architectures without having to dive too deep into the cloud implementations of those technologies/architectures
3. It's a good skill to have when working with production code - you can feel confident building integration in local dev so when you push to sandbox you can limit the amount of integration testing that happens in an environment that can block others
4. It's cheaper
5. You're likely deploying within docker images anyways (or using managed service)

## Goals
1. This repo should evolve to cover a broad range of data engineering topics, but some engineering and data modeling best practices should be addressed first
2. Subsequent concepts can easily be implemented and the project can be extended to cover them

## Where to start!
1. I named all project name's artemis - feel free to update this everywhere
2. I made a docker-compose that will run a basic application. We can do as little or as much as you want with the app itself, but we can build data pipelines that feed into the application database, consume from it, as well as more sophisticated data lifecycles
3. Before running the app, let's focus on the data model for an application that is at the heart of the data pipelines we'll be building out
   1. Pick an industry or domain that resonates with you - it can be anything, but you can stick with music streaming if you want to have it directly relate back to your job
   2. Use an ERD tool (I use StarUML since it works on mac and has a free version - there are others, some are better than others)
   3. Make a data model! We can dig into the concepts here and talk about all the decisions that go into this!
   4. Translate your data model to a DDL and put it into the file at `migrations/V0001_InitialSetup.sql`
      1. This project uses flyway for handling database migrations, and they are set up to automatically run when you run the compose file
      2. If you ever need to startover, you can just run `rm -rf .artemis` on the dir that is used as a volume mount for the project. The whole database state lives here, so it will persist even if you spin the app down and back up
4. Run the app!
   1. `docker-compose up --build` will run everything within docker. This will spin up a postgres database, the flyway migration, the core application, and an nginx proxy server to sit in front of the application
      1. This project uses pipenv for dependency management, and a flask app. There are other tools that some people like, such a poetry or django. Since our focus is a full 3 tiered app, flask allows for us to decouple the database in a way that let's us focus on the concepts of each piece independently - so for now, I would recommend sticking with flask, but feel free to swap out any tech stacks that you want! It's your playground!

## What's Next?
1. Once the data model is implemented in the database, we can talk about seeding strategies
   1. This could include a simple data seeding script or we could build out an entire data engineering pipeline - especially for populating reference data from a third party source
      1. A data ingestion pipeline can be very simple to very complex - and we can evolve it into a full datalake pattern with multiple consumers
2. Once the data is seeded, we can build a data consumer of the application data
   1. This can run from simple to more complex. We can add a zookeeper service to the docker compose and use the tech stack that you use at your job or can experiment with swapping it out for other tooling and getting the first hand experience of how they are different
3. We can dive deeper into any area that you want to - or build scaffolding for simple a->b to get a big picture idea of concepts

