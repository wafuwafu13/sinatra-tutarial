FROM ruby:latest
WORKDIR /app
RUN apt-get update && apt-get install -y \
  build-essential \
  libmariadb-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

COPY Gemfile ./
COPY Gemfile.lock ./
RUN bundle config --local set path 'vender/bundle'
RUN bundle install

CMD bundle exec ruby index.rb
